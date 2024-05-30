from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('shop',ShopView.as_view()),
     path('fircode',FIRcodeView.as_view()),
     path('fir-details',fir_page,name='fir-details'),
     path('fir/add/',add_fir_page,name='add-fir'),
     path('fir/update/<int:pk>',edit_fir,name='edit-fir'),
     path('fir/delete/<int:pk>',delete_fir,name='delete-fir'),
]
