from django.urls import re_path as url
from django.urls import path
from toolsApp.views import *

app_name = 'toolsApp'

urlpatterns = [
    path('tools/', tools, name='tools'),
    path('github-user-viewer/', githubUserView, name='githubUserView')
]