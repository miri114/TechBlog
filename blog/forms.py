from django import forms
from .models import Post,Category, Comment

# choices = [('smartphones', 'smartphones'), ('samsung', 'samsung'), ('iphone', 'iphone'),]

choices = Category.objects.all().values_list('name', 'name') # this might bring some problems since is queryset

choice_list = []

# so we do this to add themto an actual python list 
for item in choices:
    choice_list.append(item)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'post_snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'author', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'post_snippet': forms.Textarea(attrs={'class':'form-control'}),
        }


class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'post_snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'post_snippet': forms.Textarea(attrs={'class':'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }