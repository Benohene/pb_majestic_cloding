from django.contrib import admin
from .models import Blog, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'author',
        'created_on',
        'status',
        'total_likes',
    )
    
    list_filter = ('status',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'name',
        'created_on',
        'approved',
    )
    
    list_filter = ('approved',)
    search_fields = ['body']
    
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
