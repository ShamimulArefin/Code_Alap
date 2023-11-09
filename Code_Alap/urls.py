from django.contrib import admin
from django.urls import path
from django.conf.urls import include, handler404

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeApp.urls')),
    path('', include('toolsApp.urls')),
    path('', include('userApp.urls')),
    path('', include('blogApp.urls')),
]

handler404 = 'homeApp.views.notFound'

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)