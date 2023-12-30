
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
    path('logout/', logout_view, name="logout"),





]