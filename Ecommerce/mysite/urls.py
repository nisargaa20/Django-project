"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from buyer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="index"),
    path('about/', about_view, name="about"),
    path('checkout/', checkout_view, name="checkout"),
    path('contact/', contact_view, name="contact"),
    path('faqs/', faqs_view, name="faqs"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('header/', header_view, name="header"),
      path('otp/', otp_view, name="otp"),


]