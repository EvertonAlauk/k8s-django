from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from trade.decorators import token_required
from trade.models import Trade
from trade.redis_client import RedisClient
from trade.serializers import TradeSerializer
from trade.serializers import TradeCreateSerializer
from trade.serializers import BalanceSerializer


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


@method_decorator(token_required, name='dispatch')
class TradeView(ListCreateAPIView):
    queryset = Trade.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TradeCreateSerializer
        return TradeSerializer
    
    def get(self, request, user_id, *args, **kwargs):
        retrieved = self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data=retrieved.data)

    def post(self, request, user_id, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data=created.data)


@method_decorator(token_required, name='dispatch')
class BalanceView(RetrieveAPIView):
    serializer_class = BalanceSerializer
    queryset = Trade.objects.all()
    lookup_field = 'id'

    def get(self, request, user_id, *args, **kwargs):
        cache = RedisClient()
        balance = cache.get('balance')
        if not balance:
            retrieved = self.retrieve(request, *args, **kwargs)
            balance = cache.create('balance', retrieved.data)
        return Response(status=status.HTTP_200_OK, data=balance)
