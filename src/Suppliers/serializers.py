from rest_framework import serializers
from .models import *

class SuppliersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'