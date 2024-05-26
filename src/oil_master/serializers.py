from rest_framework import serializers
from .models import *

class OilMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = OilMaster
        fields = '__all__'