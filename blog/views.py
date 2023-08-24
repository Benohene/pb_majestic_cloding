from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def blog(request):
    """ A view to return the blog page """
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
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
    """ A view to return the add blog page """
    user = request.user
    if not user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = user
            blog.save()
            title = form.cleaned_data.get('title')
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
            
    else:
        form = BlogForm()
    
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    
    return render(request, template, context)
    

def edit_blog(request, blog_id):
    """ A view to return the edit blog page """
    
    return render(request, 'blog/edit_blog.html')

def delete_blog(request, blog_id):
    """ A view to return the delete blog page """
    
    return render(request, 'blog/delete_blog.html')