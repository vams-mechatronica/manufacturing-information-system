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
from .forms import *
from django.shortcuts import get_object_or_404


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
    

def fir_page(request):
    queryset = FIRcode.objects.all()
    context = {'firs':queryset}
    return render(request, 'fir/fir_codes.html', context=context)

def add_fir_page(request):
    if request.method == 'POST':
        form = FIRForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fir-details')  # Replace with your success URL or view name
    else:
        form = FIRForm()
    return render(request, 'fir/add-fir.html', {'form': form})

def edit_fir(request, pk):
    fir = get_object_or_404(FIRcode, pk=pk)
    if request.method == 'POST':
        form = FIRForm(request.POST, request.FILES, instance=fir)
        if form.is_valid():
            form.save()
            return redirect('fir-details')  # Replace with your success URL or view name
    else:
        form = FIRForm(instance=fir)
    return render(request, 'fir/edit-fir.html', {'form': form})

def delete_fir(request,id):
    fir = get_object_or_404(FIRcode, id=id) 
    fir.delete()
    return redirect('fir-details')