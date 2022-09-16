"""problog URL Configuration

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
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='back-home'),
    path('ads/', views.advertise, name='back-ads'),
    path('tech/', views.technology, name='back-tech'),
    path('make/', views.makemoney, name='back-make'),
    path('ades/<int:id>/', views.ads_des, name='ads-desc'),
    path('tdes/<int:id>/', views.tech_des, name='tech-desc'),
    path('mdes/<int:id>/', views.make_des, name='make-desc')
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

