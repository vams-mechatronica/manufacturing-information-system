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

class SuppliersView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SuppliersSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)