from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BlogForm, BlogCategoryForm
from .models import Blog, BlogCategory
from django.db.models import Count

# Create your views here.

def blogview(request):
    blogs = Blog.objects.all()
    dict = {'title':"Code Alap's Blog", 'blogs':blogs}
    return render(request, 'blogApp/blog.html', context=dict)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    dict = {'title':blog.blog_title, 'blog':blog}
    return render(request, 'blogApp/blogDetails.html', context=dict)

@login_required
def create_blog(request):
    current_user = request.user
    form = BlogForm()
    valid = False
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.author = current_user
            blog_obj.save()
            valid = True
    dict = {'title':"Write Blog", 'form': form, 'valid':valid,}
    return render(request, 'blogApp/createBlog.html', context=dict)

@login_required
def edit_blog_page(request):
    blogs = Blog.objects.all()
    dict = {'title':'Edit Blog Page', 'blogs':blogs,}
    return render(request, 'blogApp/editBlogPage.html', context=dict)

@login_required
def edit_blog_post(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = BlogForm()
    updated = False
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            form = BlogForm(instance=blog)
            updated = True
    dict = {'title':blog.blog_title, 'blog':blog, 'form': form, 'updated':updated,}
    return render(request, 'blogApp/editBlog.html', context=dict)


# Category Section
@login_required
def create_category(request):
    form = BlogCategoryForm()
    created = False
    if request.method == 'POST':
        form = BlogCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            created = True
    dict = {'title':'Create Category', 'form': form, 'created': created}
    return render(request, 'blogApp/addCategory.html', context=dict)

@login_required
def edit_category(request, slug):
    category = BlogCategory.objects.get(cat_slug=slug)
    form = BlogCategoryForm(instance=category)
    updated = False
    if request.method == 'POST':
        form = BlogCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            form = BlogCategoryForm(instance=category)
            updated = True
    dict = {'title':'Edit Category', 'category':category, 'form': form, 'updated': updated}
    return render(request, 'blogApp/editCategory.html', context=dict)

def single_category(request, slug):
    category = BlogCategory.objects.get(cat_slug=slug)
    posts = Blog.objects.all().filter(blog_category=category)
    dict = {'title':category.cat_name, 'category':category, 'posts': posts,}
    return render(request, 'blogApp/singleCategory.html', context=dict)

def all_categories(request):
    categories = BlogCategory.objects.all().annotate(posts_count=Count('post_category'))
    dict = {'title':'Categories of Code Alap', 'categories':categories,}
    return render(request, 'blogApp/allCategories.html', context=dict)
