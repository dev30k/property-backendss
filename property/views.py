from rest_framework.response import Response
from django.shortcuts import render
from .models import Business
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BusinessSerializer


class PropertyView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BusinessSerializer
    def post(self,request):

        serializer  = BusinessSerializer(data = request.data)
        if serializer.is_valid():
            business_name = serializer.validated_data['business_name']
            payment_account_number = serializer.validated_data['payment_account_number']
            property_description = serializer.validated_data['property_description']

            business = Business.objects.create(
                business_name=business_name,
                payment_account_number=payment_account_number,
                property_description=property_description,
                owner=request.user,
            )

            business.save()

            response_content = {
                'status': True,
                'message': 'Businss added successfully.',
            }

            return Response(response_content, status=status.HTTP_200_OK)

        else:
            response_content = {
                'status': False,
                'message': serializer.errors,
            }

            print(response_content)
            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)
