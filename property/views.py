from rest_framework.response import Response
from django.shortcuts import render
from .models import Property
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PropertySerializer,ResidentailPropertSerializer


class PropertyView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertySerializer
    def post(self,request):
        request.data['landlord']=request.user.pk
        serializer  = PropertySerializer(data = request.data)
        if serializer.is_valid():
            saved = serializer.save()
            response_content = {
                'status': True,
                'message': 'Property added successfully.',
                'property': saved.id
            }
            return Response(response_content, status=status.HTTP_200_OK)
        else:
            response_content = {
                'status': False,
                'message': serializer.errors,
            }

            print(response_content)
            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data = Property.get_property(request.user.first_name)
        serializer = PropertySerializer(data,many = True)
        response_content = {
                'status': True,
                'message': 'Property listing.',
                'property': serializer.data
            }
        return Response(response_content, status=status.HTTP_200_OK)

class ResidentialPropertyView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertySerializer

    def post(self,request):
        print(request.data)
        for residential_data in request.data:

            serializer  = ResidentailPropertSerializer(data=residential_data)
            if serializer.is_valid():
                serializer.save()

            else:
                response_content = {
                    'status': False,
                    'message': serializer.errors,
                }
                return Response(response_content, status=status.HTTP_400_BAD_REQUEST)

        response_content = {
            'status': True,
            'message': 'Residential added successfully.',
        }
        return Response(response_content, status=status.HTTP_200_OK)

    def get(self,request):
        data = Property.get_property(request.user.first_name)
        serializer = PropertySerializer(data,many = True)
        return Response(serializer.data)
        
    pass