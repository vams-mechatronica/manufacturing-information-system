from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('equipment',EquipmentView.as_view()),
     path('equipment-spare-parts',EquipmentSpareView.as_view()),
]
