from .models import *
from .serializers import *
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render,redirect
from django_filters.rest_framework import DjangoFilterBackend
from .filters import LargeResultsSetPagination
from django.shortcuts import get_object_or_404

# Create your views here.
class EquipmentView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EquipmentSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class EquipmentSpareView(generics.ListCreateAPIView):
    queryset = EquipmentSpare.objects.all()
    serializer_class = EquipmentSpareSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EquipmentSpareSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

def equipments_view(request):
    equipments = Equipment.objects.all()
    context = {'equipments':equipments}
    return render(request, 'equipments.html', context)


def equipmentspares_view(request):
    spares = EquipmentSpare.objects.all()
    context = {'spares':spares}
    return render(request, 'equipments-spares.html', context)

def delete_equipments_view(request,id):
    equipment = get_object_or_404(Equipment, id=id) 
    equipment.delete()
    return redirect('equipment-view')

from .forms import EquipmentForm

def add_record(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipment-view')  # Replace with your success URL or view name
    else:
        form = EquipmentForm()
    return render(request, 'add-equipment.html', {'form': form})