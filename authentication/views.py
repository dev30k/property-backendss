from rest_framework.response import Response
from users.models import MyUser
from users.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        """
        sign up funtion.
        taking in  first_name,email,last_name,password to make a new user
        """
        serializer = RegistrationSerializer(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })
