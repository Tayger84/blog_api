from django.urls import path
from .views import PostList, PostDetail, post_form

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('create-post/', post_form, name='post-form'),
]