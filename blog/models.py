from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        #after creating new post it will redirect us to the post we just created
        # return reverse('blog_detail', args=(str(self.id)))
        
        ## we can just return to home with this 
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=300)
    title_tag = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    blogpost_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=300, default='smartphones')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #after creating new post it will redirect us to the post we just created
        # return reverse('blog_detail', args=(str(self.id)))
        
        ## we can just return to home with this 
        return reverse('home')

