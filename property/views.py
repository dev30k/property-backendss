from rest_framework.response import Response
from django.shortcuts import render
from .models import Property
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PropertySerializer


class PropertyView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertySerializer
    def post(self,request):

        serializer  = PropertySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(landlord =request.user)

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
