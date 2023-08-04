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


class ShopView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FIRcodeView(generics.ListCreateAPIView):
    queryset = FIRcode.objects.all()
    serializer_class = FIRcodeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FIRcodeSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)