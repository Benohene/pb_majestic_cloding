"""Admin page  for blog app"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment


class BlogAdmin(SummernoteModelAdmin):
    """Admin content for blog"""

    list_display = (
        "title",
        "author",
        "created_on",
        "status",
        "total_likes",
    )

    list_filter = ("status",)
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("body",)


class CommentAdmin(admin.ModelAdmin):
    """Admin content for comments"""

    list_display = (
        "blog",
        "name",
        "created_on",
    )

    search_fields = ["body"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
