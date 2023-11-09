from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class BlogCategory(models.Model):
    cat_name = models.CharField(max_length=200,)
    cat_slug = models.SlugField(max_length=264, unique=True,)
    cat_description = models.CharField(max_length=160,)
    cat_image = models.URLField(max_length=200,)
    cat_image_up = models.ImageField(upload_to='cat_images', blank=True)

    def __str__(self):
        return self.cat_name

class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.DO_NOTHING)
    blog_category = models.ForeignKey(BlogCategory, related_name='post_category', null=True, on_delete=models.DO_NOTHING)
    blog_title = models.CharField(max_length=264,)
    slug = models.SlugField(max_length=264, unique=True)
    blog_description = models.CharField(max_length=160,)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images', blank=True)
    image_url = models.URLField(max_length=160, )
    blog_tags = models.CharField(max_length=200,)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.blog_title