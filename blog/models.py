from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    title_tag = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()


    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #after creating new post it will redirect us to the post we just created
        # return reverse('blog_detail', args=(str(self.id)))
        
        ## we can just return to home with this 
        return reverse('home')

