from .models import MyUser
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = '__all__'

        extra_kwargs = {"password": {"write_only": True}}