from django.urls import path
#from . import views
from . views import HomeView, BlogDetailView, AddBlogPostView, UpdateBlogPostView,DeleteBlogPostView,AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    #path('', views.home, name='home'),  # this urls is used when work with function based view
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog_post/', AddBlogPostView.as_view(), name='add_blog_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('blog/edit/<int:pk>', UpdateBlogPostView.as_view(), name='update_blog_post'),
    path('blog/<int:pk>/remove', DeleteBlogPostView.as_view(), name='delete_blog_post'),
    path('category/<str:catgs>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
