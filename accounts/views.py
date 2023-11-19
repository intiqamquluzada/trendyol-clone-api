from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import LoginSerializer, RegisterSerializer, VerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from accounts.models import User
from rest_framework.response import Response
from accounts.emails import send_otp_w_mail

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
        send_otp_w_mail(serializer.data['email'])

        return Response(serializer.data, status=201)


class VerifyAPI(APIView):
    def post(self, request):

        data = request.data
        serializer = VerifySerializer(data=data)

        if serializer.is_valid():
            email = serializer.data['email']
            otp = serializer.data['otp']
            user = User.objects.filter(email=email)
            if not user.exists():
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': 'invalid email'
                })
            if not user[0].activate_code == otp:
                return Response({
                    "status": 400,
                    "message": "something went wrong",
                    'data': 'wrong otp'
                })
            user = user.first()
            user.is_active = True
            user.save()
            return Response({
                "status": 200,
                "message": "account verified",
                "data": user.email
            })




def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "Logged out"}, status=201)
