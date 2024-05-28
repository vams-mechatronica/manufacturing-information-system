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
    
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-supplier')  # Replace with your success URL or view name
    else:
        form = SupplierForm()
    return render(request, 'suppliers/add-suppliers.html', {'form': form})


def suppliers_view(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers':suppliers}
    return render(request, 'suppliers/suppliers.html', context)


def delete_suppliers_view(request,id):
    suppliers = get_object_or_404(Supplier, id=id) 
    suppliers.delete()
    return redirect('supplier-view')

def edit_supplier(request, pk):
    suppliers = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=suppliers)
        if form.is_valid():
            form.save()
            return redirect('supplier-view')  # Replace with your success URL or view name
    else:
        form = SupplierForm(instance=suppliers)
    return render(request, 'suppliers/edit.html', {'form': form})