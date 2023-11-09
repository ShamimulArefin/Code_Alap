from django.urls import path
from . import views

app_name = 'blogApp'

urlpatterns = [
    # category
    path('add-category/', views.create_category, name='createCategory'),
    path('edit-category/<slug:slug>/', views.edit_category, name='editCategory'),
    path('category/<slug:slug>/', views.single_category, name='singleCategory'),
    path('category/', views.all_categories, name='allCategories'),

    # blog
    path('blog/', views.blogview, name='blog'),
    path('create-blog/', views.create_blog, name='createBlog'),
    path('edit-blog/', views.edit_blog_page, name='editBlogPage'),
    path('edit-blog/<slug:slug>/', views.edit_blog_post, name='editBlogPost'),
    path('<slug:slug>/', views.blog_details, name='blogDetails'),
]