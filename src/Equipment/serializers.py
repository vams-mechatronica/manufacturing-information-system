from rest_framework import serializers
from .models import *

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentSpareSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentSpare
        fields = '__all__'

class MachineStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineStatus
        fields = '__all__'