from .models import Property
from rest_framework import serializers
from rest_framework import status

class PropertySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property
        fields="__all__"

    def create(self, validated_data,instance):
        landlord=validated_data.pop['landlord'],
        user = Property(
            property_image=validated_data['property_image'],
            units=validated_data['units'],
            property_type=validated_data['property_type'],
            number_of_units=validated_data['number_of_units'],
            county=validated_data['county'],
            address=validated_data['address'],
            property_name=validated_data['property_name']
        )
        user.save(landlord =instance)
        return user
    