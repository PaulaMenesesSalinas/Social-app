from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView,CreateView
from .form import UserForm,PostForm
from .models import User, Post
from django.urls import reverse_lazy

class HomePageview(TemplateView):
    template_name = "app_06/home.html"


class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "app_06/user_list.html"


class UserDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "app_06/user_profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    # pk_url_kwarg='user_id'
    # localhost/users/username/


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "app_06/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "app_06/post_detail.html"
    pk_url_kwarg = "post_id"
    # localhost/app/posts/id
    
class UserPostView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name ='app_06/user_posts.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        print(context)
        print('#'*50)
        username = self.kwargs['username']
        user = get_object_or_404(User,username=username)      
        context['user']=user
        print(context)
        return context
    
    def get_queryset(self) :
        username = self.kwargs['username']
        user = get_object_or_404(User,username=username)
        #displaying the data at this order
        return Post.objects.filter(user=user).order_by('-created_at')
    
class RegisterUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'app_06/register.html'
    success_url = reverse_lazy('users-list')
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app_06/post_create.html'
    
    def form_valid(self, form):  
        user = get_object_or_404(User,username=self.kwargs['username'])
        form.instance.user = user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('user-detail',kwargs={'username':self.object.user.username})
    
    
    
        
