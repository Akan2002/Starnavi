from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
User = get_user_model()

from rest_framework.viewsets import ModelViewSet
from mainapp.models import(
    User, SmsUser,
)
from mainapp.serializer import(
    UserSerializer, SmsUserSerializer, RegistrationSerializer, AuthorizationSeriaizer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SmsUserView(ModelViewSet):
    queryset = SmsUser.objects.all()
    serializer_class = SmsUserSerializer

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        serializer.is_valid(raice_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username = username).exists():
            return Response({'message': 'Username with such username is already exist'})
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
        )
class AuthorizationView(APIView):
    def post(self, request):
        serializer = AuthorizationSeriaizer(data = request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User is not None:
            if check_password(password, User.password):
                token, _=Token.objects.get_or_create(User=User)
                return Response({'token':token.key})
            return Response({'error': 'Password is not vallid'}, status=400)
        return Response({'error': 'username is not registered'}, status=400)

