from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category
# Create your views here.
from .forms import BlogPostForm, EditBlogPostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'
    ordering=['-blogpost_date']

def CategoryView(request, catgs):
    category_posts = Post.objects.filter(category=catgs)
    return render(request, 'categories.html', {'catgs':catgs.title(), 'category_posts': category_posts })

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class AddBlogPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'
    #fields = '__all__'     # since we creating new post, this takes all fields of a post defined in models.py 

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'     # since we creating new category, this takes all fields of a category defined in models.py 

class UpdateBlogPostView(UpdateView):
    model = Post
    form_class = EditBlogPostForm
    template_name = 'update_blog_post.html'
    # fields = ('title', 'title_tag', 'body')

class DeleteBlogPostView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('home')
    