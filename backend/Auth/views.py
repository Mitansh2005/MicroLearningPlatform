from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (
    UserRegisterationSerializer,
    CustomUserLoginSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
)
from django.contrib.auth import authenticate
from Auth.renderers import CustomUserRenders
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserRegisteration(APIView):
    renderer_classes = [CustomUserRenders]

    def post(self, request, format=None):
        serializer = UserRegisterationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                { "msg": "Registeration success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    renderer_classes = [CustomUserRenders]

    def post(self, request, format=None):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response(
                    { "msg": "login was successful"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"msg": "Email or Password is not valid"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [CustomUserRenders]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeUserPassword(APIView):
    renderer_classes = [CustomUserRenders]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "Password is successfully changed"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
