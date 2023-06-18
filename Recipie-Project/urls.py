"""Recipie-Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Recipie_App.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', base_html, name="base_html"),
    path('aboutus/', aboutus, name='aboutus'),
    path('admin/', admin.site.urls),
    path('recipies/', recipies, name="recipies"),
    path('view_recipies/', view_recipies, name="view_recipies"),
    path('delete_recipie/<id>/', delete_recipie, name="delete_recipie"),
    path('update_recipie/<id>/', update_recipie, name="update_recipie"),
    path('login/', login_page, name="login_page"),
    path('register/', register, name="register"),
    path('logout/', logout_page, name="logout_page"),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()