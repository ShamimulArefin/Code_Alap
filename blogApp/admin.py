from django.contrib import admin
from .models import Blog, BlogCategory
# Register your models here.
admin.site.register(BlogCategory)
admin.site.register(Blog)
