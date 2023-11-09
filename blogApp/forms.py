from django import forms
from .models import Blog, BlogCategory


class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['cat_name', 'cat_slug', 'cat_description', 'cat_image',]
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'blog_category', 'blog_title', 'slug', 'blog_description', 'image_url', 'blog_tags', 'blog_content',]
