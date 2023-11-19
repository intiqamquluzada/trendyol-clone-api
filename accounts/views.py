from django.shortcuts import render
from accounts.serializers import LoginSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from accounts.models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  # Import make_password function


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        user = User.objects.get(email=email)

        token = RefreshToken.for_user(user)

        data = {
            **serializer.data,
            "refresh": str(token),
            "access": str(token.access_token)

        }

        return Response(data, status=201)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(serializer.data, status=201)


def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "Logged out"}, status=201)
