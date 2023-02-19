from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class AddBlogPostView(CreateView):
    model = Post
    template_name = 'add_blog_post.html'
    fields = '__all__'     # since we creating new post, this takes all fields of a post defined in models.py 

