from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('home/',home,name="home"),
     path('home/master/',master,name="master"),
     path('home/maintenance/',master,name="maintenance"),
     path('home/reports/',reports,name="reports"),
     path('home/amc/',master,name="amc"),

     path('login/',loginRequest,name='login'),
     path('logout/',logoutRequest,name='logout'),
]
