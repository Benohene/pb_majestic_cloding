from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
from django.contrib.auth.models import User

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
    
    if blog.likes.filter(id=user.id).exists():
        liked = True
    
    template = 'blog/blog_detail.html'
    context = {
        'blog': blog,
        'liked': liked,
    }
    
    return render(request, template, context)

def add_blog(request):
    """ A view to return the add blog page """
    
    return render(request, 'blog/add_blog.html')

def edit_blog(request, blog_id):
    """ A view to return the edit blog page """
    
    return render(request, 'blog/edit_blog.html')

def delete_blog(request, blog_id):
    """ A view to return the delete blog page """
    
    return render(request, 'blog/delete_blog.html')