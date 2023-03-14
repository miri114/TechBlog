from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category, Comment
# Create your views here.
from .forms import BlogPostForm, EditBlogPostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    #liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        #liked = False
    else:
        post.likes.add(request.user)
        #liked = True
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'
    ordering=['-blogpost_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context ["cat_menu"] = cat_menu
        return context

def CategoryView(request, catgs):
    category_posts = Post.objects.filter(category=catgs.replace('-',' '))
    return render(request, 'categories.html', {'catgs':catgs.title().replace('-',' '), 'category_posts': category_posts })

def CategoryListView(request):
    catg_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'catg_menu_list':catg_menu_list})

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)

        things = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = things.total_likes()

        liked = False
        if things.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

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


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # success_url = reverse_lazy("home")
    # fields = '__all__'     

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk']})