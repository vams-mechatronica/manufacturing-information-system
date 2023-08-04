from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('shop',ShopView.as_view()),
     path('fircode',FIRcodeView.as_view()),
]
