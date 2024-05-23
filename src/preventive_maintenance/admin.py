from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PMActivityMaster)
class PMActivityMasterAdmin(admin.ModelAdmin):
    pass

@admin.register(PMSchedule)
class PMScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(PMScheduleFeedback)
class PMScheduleFeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(OilMaster)
class OilMasterAdmin(admin.ModelAdmin):
    pass
    

    

    

    
