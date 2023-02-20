from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.
from .forms import BlogPostForm, EditBlogPostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'
    ordering=['-id']

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class AddBlogPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'
    #fields = '__all__'     # since we creating new post, this takes all fields of a post defined in models.py 

class UpdateBlogPostView(UpdateView):
    model = Post
    form_class = EditBlogPostForm
    template_name = 'update_blog_post.html'
    # fields = ('title', 'title_tag', 'body')

class DeleteBlogPostView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('home')
    