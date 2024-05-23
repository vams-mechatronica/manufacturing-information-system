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
from Manufacturer.filters import LargeResultsSetPagination
from datetime import datetime, timedelta
import calendar
from django.db.models import Sum



class PMActivityMasterView(generics.ListCreateAPIView):
    queryset = PMActivityMaster.objects.all()
    serializer_class = PMActivityMasterSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PMActivityMasterSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PMScheduleView(generics.ListCreateAPIView):
    queryset = PMSchedule.objects.all()
    serializer_class = PMScheduleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PMScheduleFeedbackView(generics.ListCreateAPIView):
    queryset = PMScheduleFeedback.objects.all()
    serializer_class = PMScheduleFeedbackSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class OilMasterView(generics.ListCreateAPIView):
    queryset = OilMaster.objects.all()
    serializer_class = OilMasterSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class BreakDownView(generics.ListCreateAPIView):
    queryset = BreakDown.objects.all()
    serializer_class = BreakDownSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class MachineAvailabilityAPIView(APIView):
    def get(self, request, *args, **kwargs):
        machine_name = request.GET.get('machine_name', None)
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        if machine_name and year:
            return self.get_yearly_availability(machine_name, int(year))
        elif machine_name and month:
            return self.get_monthly_availability(machine_name, int(month))
        elif start_date and end_date:
            return self.get_date_range_availability(start_date, end_date)
        else:
            return Response({"error": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_yearly_availability(self, machine_name, year):
        machine = Equipment.objects.get(name=machine_name)
        availability = []

        for i in range(10):
            current_year = year - i
            breakdown_hours = BreakDown.objects.filter(machine=machine, break_down_date__year=current_year).aggregate(Sum('total_breakdown_hrs'))['total_breakdown_hrs__sum'] or 0
            total_hours = 365 * 24
            percentage_availability = ((total_hours - breakdown_hours) / total_hours) * 100
            availability.append({'year': current_year, 'availability': percentage_availability})

        return Response(availability, status=status.HTTP_200_OK)
    
    def get_monthly_availability(self, machine_name, month):
        machine = Equipment.objects.get(name=machine_name)
        availability = []
        current_date = datetime.now()

        for i in range(10):
            target_month = (current_date.month - i) % 12 or 12
            target_year = current_date.year - ((current_date.month - i - 1) // 12)
            days_in_month = calendar.monthrange(target_year, target_month)[1]
            breakdown_hours = BreakDown.objects.filter(machine=machine, break_down_date__year=target_year, break_down_date__month=target_month).aggregate(Sum('total_breakdown_hrs'))['total_breakdown_hrs__sum'] or 0
            total_hours = days_in_month * 24
            percentage_availability = ((total_hours - breakdown_hours) / total_hours) * 100
            availability.append({'year': target_year, 'month': target_month, 'availability': percentage_availability})

        return Response(availability, status=status.HTTP_200_OK)
    
    def get_date_range_availability(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        delta = timedelta(days=1)
        availability = []

        current_date = start_date
        machines = Equipment.objects.all()

        while current_date <= end_date:
            next_month = current_date.replace(day=28) + timedelta(days=4)
            last_day_of_month = next_month - timedelta(days=next_month.day)

            for machine in machines:
                breakdown_hours = BreakDown.objects.filter(machine=machine, break_down_date__year=current_date.year, break_down_date__month=current_date.month).aggregate(Sum('total_breakdown_hrs'))['total_breakdown_hrs__sum'] or 0
                total_hours = last_day_of_month.day * 24
                percentage_availability = ((total_hours - breakdown_hours) / total_hours) * 100
                availability.append({
                    'machine': machine.number,
                    'year': current_date.year,
                    'month': current_date.month,
                    'availability': percentage_availability
                })

            current_date = last_day_of_month + delta

        return Response(availability, status=status.HTTP_200_OK)