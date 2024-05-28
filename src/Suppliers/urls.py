from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('api/view',SuppliersView.as_view()),
     path('add',add_supplier,name="add-supplier"),
     path('view',suppliers_view,name="suppliers-view"),
     path('delete/<str:pk>',delete_suppliers_view,name="delete-supplier"),
     path('update/<str:pk>',edit_supplier,name="edit-supplier"),
]
