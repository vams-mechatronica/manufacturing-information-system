from .models import *
from .serializers import *
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .filters import LargeResultsSetPagination

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