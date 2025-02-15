from rest_framework.generics import CreateAPIView # https://www.django-r
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request # https://www.django-rest-fra
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer , PasswordResetSerializer
from rest_framework import status , generics
from django.contrib.auth.views import PasswordResetView



class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Thanks for registration!'})
    

class ActivationView(CreateAPIView):
    serializer_class = ActivationSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = ActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response({'message': 'Аккаунт успешно активирован!'})


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request) -> Response:
        Token.objects.get(user=request.user).delete()
        return Response({'message': 'Logged out'})
    
class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Письмо с инструкциями по восстановлению пароля было отправлено на ваш email"},
            status=status.HTTP_200_OK,
        )



























