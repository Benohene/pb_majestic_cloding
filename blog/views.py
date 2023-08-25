''' This file is used to create the views for the blog app.'''
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required



def blog(request):
    """ A view to return the blog page """
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    template = 'blog/blog.html'
    context = {
        'blogs': paged_blogs,
    }

    return render(request, template, context)


def blog_detail(request, blog_id):
    """ A view to return the blog detail page """
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    liked = False
    if user.is_authenticated:
        if blog.likes.filter(id=user.id).exists():
            liked = True

    template = 'blog/blog_detail.html'
    context = {
        'blog': blog,
        'liked': liked,
    }

    return render(request, template, context)


def like_blog(request, blog_id):
    """ A view to return the like blog page """
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    liked = False
    
    if user.is_authenticated:
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            liked = False
            messages.success(request, 'You have unliked this blog')
        else:
            blog.likes.add(request.user)
            liked = True
            messages.success(request, 'You have liked this blog')
    else:
        messages.warning(request, 'You need to login to like this blog')
        return render(request, 'account/login.html')
                  
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'liked': liked})


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
                messages.success(
                    request, f"Successfully added blog post - {title}."
                )
                return redirect(reverse("blog_detail", args=[blog.id]))
            else:
                messages.error(
                    request,
                    (
                        "Failed to add blog post. "
                        "Please ensure the form is valid."
                    ),
                )
        else:
            form = BlogForm()

    template = "blog/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def edit_blog(request, blog_id):
    """ A view to return the edit blog page """
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
                    (
                        "Failed to update blog post. "
                        "Please ensure the form is valid."
                    ),
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


def delete_blog(request, blog_id):
    """ A view to return the delete blog page """
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
