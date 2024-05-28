from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('equipment',EquipmentView.as_view()),
     path('equipment-details',equipments_view,name="equipment-view"),
     path('equipment/add/', add_record, name='add-equipment'),
     path('equipment/delete/<int:id>',delete_equipments_view,name="delete_equipment"),
     path('equipment/update/<int:pk>',edit_equipment,name="edit_equipment"),
     path('equipment-spare-parts',EquipmentSpareView.as_view()),
     path('equipment-spares-details',equipmentspares_view,name="equipment-spares-details"),
]
