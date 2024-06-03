from django.urls import path, include
from .views import (
    HomePageview,
    UserListView,
    UserDetailView,
    PostListView,
    PostDetailView,
    UserPostView,
    RegisterUserView,PostCreateView
)

urlpatterns = [
    path("", HomePageview.as_view(), name="home"),
    path("users/", UserListView.as_view(), name="users-list"),
    path("users/<str:username>/", UserDetailView.as_view(), name="user-detail"),
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/<int:post_id>/", PostDetailView.as_view(), name="post-detail"),
    path('users/<str:username>/posts/',UserPostView.as_view(),name='user-posts'),
    path('register/',RegisterUserView.as_view(),name='register'),
    path('users/post/<str:username>/',PostCreateView.as_view(),name='create-post')
]
# path('url/',views,name_for_html_h)
