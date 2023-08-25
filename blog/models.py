from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    image = ResizedImageField(size=[800, 600], upload_to='blog/images', blank=True, null=True, quality=75, verbose_name='Image', help_text='Image size must be 800x600px', force_format='JPEG')
    image_url = models.URLField(max_length=2024, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, null=False, blank=False)
    body = models.TextField(null=False, blank=False, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
