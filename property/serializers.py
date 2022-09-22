from .models import Property,ResidentailProperty
from rest_framework import serializers
from rest_framework import status

class PropertySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property
        fields="__all__"


class ResidentailPropertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentailProperty
        fields = "__all__"
