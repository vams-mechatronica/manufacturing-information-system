from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('hsd-details',oil_page,name="oil-hsd-details"),
     path('oil-master',OilMasterView.as_view()),
]
