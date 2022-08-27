from .models import Business
from rest_framework import serializers
from rest_framework import status

class BusinessSerializer(serializers.Serializer):
    
    business_name = serializers.CharField(error_messages={'message': 'Business name is required.'})
    payment_account_number = serializers.CharField(error_messages={'message': 'Account number is required.'})
    property_description = serializers.CharField()

    def validate(self, data):
        business_name = data.get('business_name')
        payment_account_number = data.get('payment_account_number')
        property_description = data.get('property_description')

        if not business_name or not payment_account_number:
             raise serializers.ValidationError('Fill all the fields.')
        
        return data
    