from rest_framework import serializers
from .models import *

class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

class FIRcodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FIRcode
        fields = '__all__'