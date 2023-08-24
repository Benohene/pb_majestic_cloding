from django.shortcuts import render

# Create your views here.
def blog(request):
    """ A view to return the blog page """
    
    return render(request, 'blog/blog.html')

def blog_detail(request, blog_id):
    """ A view to return the blog detail page """
    
    return render(request, 'blog/blog_detail.html')

def add_blog(request):
    """ A view to return the add blog page """
    
    return render(request, 'blog/add_blog.html')

def edit_blog(request, blog_id):
    """ A view to return the edit blog page """
    
    return render(request, 'blog/edit_blog.html')

def delete_blog(request, blog_id):
    """ A view to return the delete blog page """
    
    return render(request, 'blog/delete_blog.html')