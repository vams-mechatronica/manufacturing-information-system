from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('activity-master',PMActivityMasterView.as_view()),
     path('schedule',PMScheduleView.as_view()),
     path('schedule-feedback',PMScheduleFeedbackView.as_view()),
     path('oil-master',OilMasterView.as_view()),
     path('break-down', BreakDownView.as_view()),
     path('machine-availability', MachineAvailabilityAPIView.as_view()),
]
