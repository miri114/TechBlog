from django.urls import path
#from . import views
from . views import HomeView, BlogDetailView, AddBlogPostView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog_post/', AddBlogPostView.as_view(), name='add_blog_post'),
]
