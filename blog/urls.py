from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('<int:blog_id>/like_blog/', views.like_blog, name='like_blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
