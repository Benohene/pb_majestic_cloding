""" This file is used to create the views for the blog app."""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import BlogForm, CommentForm


def blog(request):
    """A view to return the blog page"""
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page = request.GET.get("page")
    paged_blogs = paginator.get_page(page)

    template = "blog/blog.html"
    context = {
        "blogs": paged_blogs,
    }

    return render(request, template, context)


def blog_detail(request, blog_id):
    """A view to return the blog detail page"""
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    liked = False
    comments = Comment.objects.filter(blog=blog).order_by("-created_on")

    if user.is_authenticated:
        if blog.likes.filter(id=user.id).exists():
            liked = True

    template = "blog/blog_detail.html"
    context = {
        "blog": blog,
        "liked": liked,
        "comments": comments,
        "on_blog_detail_page": True,
    }

    return render(request, template, context)


def like_blog(request, blog_id):
    """A view to return the like blog page"""
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)

    if user.is_authenticated:
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            messages.success(request, f"{user} you have unliked this Blog post.")
        else:
            blog.likes.add(request.user)
            messages.success(request, f"{user} you have liked this Blog post.")
    else:
        messages.warning(request, "You need to login to like this blog")
        return render(request, "account/login.html")

    return redirect(reverse("blog_detail", args=[blog.id]))


@login_required
def add_blog(request):
    """Add a blog post to the site"""

    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    if user.is_superuser:
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = user
                blog.save()
                title = form.cleaned_data["title"]
                messages.success(request, f"Successfully added blog post - {title}.")
                return redirect(reverse("blog_detail", args=[blog.id]))
            else:
                messages.error(
                    request,
                    ("Failed to add blog post. " "Please ensure the form is valid."),
                )
        else:
            form = BlogForm()

    template = "blog/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """A view to return the edit blog page"""
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    if user.is_superuser:
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES, instance=blog)
            if form.is_valid():
                form.save()
                messages.success(
                    request, f"Successfully updated blog post - {blog.title}."
                )
                return redirect(reverse("blog_detail", args=[blog.id]))
            else:
                messages.error(
                    request,
                    ("Failed to update blog post. " "Please ensure the form is valid."),
                )
        else:
            form = BlogForm(instance=blog)
            messages.info(request, f"You are editing {blog.title}")

    template = "blog/edit_blog.html"
    context = {
        "form": form,
        "blog": blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """A view to return the delete blog page"""
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    if user.is_superuser:
        blog.delete()
        messages.success(request, f"Blog post {blog.title} has been deleted!")
        return redirect(reverse("blog"))


def add_comment_to_blog(request, blog_id):
    """Add a comment to a blog post"""
    blog = get_object_or_404(Blog, pk=blog_id)

    if not request.user.is_authenticated:
        messages.error(request, "You need to login to comment on this blog")
        return render(request, "account/login.html")

    # if user comment on blog post exists raise error
    comments_exist = Comment.objects.filter(blog=blog).exists()
    if comments_exist:
        messages.error(request, "You have already commented on this blog")
        return redirect(reverse("blog_detail", args=[blog.id]))
    else:
        if request.method == "POST":
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.save()
                messages.success(request, "Successfully added comment!")
                return redirect(reverse("blog_detail", args=[blog.id]))
            else:
                messages.error(
                    request, "Failed to add comment. Please ensure the form is valid."
                )
        else:
            form = CommentForm()

        template = "blog/comment_blog.html"
        context = {
            "blog": blog,
            "form": form,
            "comments_exist": comments_exist,
        }

        return render(request, template, context)
    
    
def edit_comment(request, blog_id, comment_id):
    """
    Checks the database for the comment.id and then confirms if
    user matches the comment user before allowing user to edit their comment
    """
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if user.is_superuser or user == comment.name:
        if request.method == "POST":
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.save()
                messages.success(
                    request, f"{user.username} your comment has been updated"
                )

                return redirect(reverse("blog_detail", args=[blog.id]))
            else:
                messages.error(
                    request,
                    "Comment updated failed, please review the form.",
                )
        else:
            form = CommentForm(instance=comment)

    else:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect(reverse("blog_detail", args=[blog.id]))

    context = {
        "form": form,
        "blog": blog,
        "comment": comment,
    }

    return render(request, "blog/edit_comment.html", context)


def delete_comment(request, blog_id, comment_id):
    """A view to delete a comment from a blog post"""
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if user.is_superuser or user == comment.name:
        comment.delete()
        messages.success(request, "Comment deleted!")
        return redirect(reverse("blog_detail", args=[blog.id]))
    else:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect(reverse("blog_detail", args=[blog.id]))