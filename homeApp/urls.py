from django.urls import re_path as url
from django.urls import path
from homeApp.views import *

app_name = 'homeApp'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('view-contacts/', viewMessages, name='viewMessages'),
    path('delete-message/<int:message_id>/', deleteMessage, name='deleteMessage'),
]

