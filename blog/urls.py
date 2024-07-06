from django.urls import path
from . import views
from .views import (Blog_list_view,Blog_Detail_View,
Blog_Create_View,Blog_Update_View,Blog_Delete_View,UserBlog_list_view)

urlpatterns = [
    
    path('',Blog_list_view.as_view() ,name='blog.home'),
    path('blog/<int:pk>/', Blog_Detail_View.as_view(),name='blog.detail'),
    path('blog/new/', Blog_Create_View.as_view(),name='blog.content'),
    path('blog/<int:pk>/update/', Blog_Update_View.as_view(),name='blog.update'),
    path('blog/<int:pk>/delete/', Blog_Delete_View.as_view(),name='blog.delete'),
    path('blog/user/<str:username>/', UserBlog_list_view.as_view(),name='blog.user'),
    path('about/', views.about,name='blog.about'),
    
]