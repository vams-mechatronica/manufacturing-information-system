from rest_framework import serializers
from .models import *

class PMActivityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PMActivityMaster
        fields = '__all__'

class PMScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = PMSchedule
        fields = '__all__'

class PMScheduleFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = PMScheduleFeedback
        fields = '__all__'
    
class OilMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = OilMaster
        fields = '__all__'

class BreakDownSerializer(serializers.ModelSerializer):

    class Meta:
        model = BreakDown
        fields = '__all__'