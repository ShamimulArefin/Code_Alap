from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('singin/', views.sign_in, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='editProfile'),
    path('author/<username>/', views.author_profile, name='authorProfile'),
]