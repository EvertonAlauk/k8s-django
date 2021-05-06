import jwt

from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication

from core.serializers import UserSerializer


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


class AuthView(APIView):
    authentication_classes = [BasicAuthentication]

    def get(self, request, format=None):
        if request.user:
            token = jwt.encode({
                "id": request.user.id}, settings.SECRET_KEY)
            return Response({'token': token})
        return Response({'status': False})



class UserView(ListAPIView, CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get(self, request, *args, **kwargs):
        listed = self.list(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=listed.data)

    def post(self, request, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=created.data)

