"""blogpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
<<<<<<< HEAD
    url(r'^', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),

=======
    url(r'^', include('blog.urls'))
>>>>>>> 914a5b8767bb3fb05ae452eaeb88e4c6372c5da0
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
<<<<<<< HEAD
    urlpatterns += static('/contact/static/', document_root=settings.STATIC_ROOT)
=======
>>>>>>> 914a5b8767bb3fb05ae452eaeb88e4c6372c5da0

# admin
# qwertyuiop1890
