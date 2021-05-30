from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from credit.decorators import token_required
from credit.models import Limit
from credit.serializers import LimitSerializer
from credit.serializers import LimitCreateSerializer
from credit.serializers import LimitUpdateSerializer


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


@method_decorator(token_required, name='dispatch')
class LimitView(RetrieveUpdateAPIView, CreateAPIView):
    queryset = Limit.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LimitCreateSerializer
        elif self.request.method == "PATCH":
            return LimitUpdateSerializer
        return LimitSerializer
    
    def get(self, request, user_id, *args, **kwargs):
        retrieved = self.retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data=retrieved.data)

    def post(self, request, user_id, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data=created.data)
    
    def patch(self, request, user_id, *args, **kwargs):
        updated = self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data=updated.data)
