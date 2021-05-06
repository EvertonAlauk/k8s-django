from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from bank.models import Account
from bank.models import Balance
from bank.models import Credit
from bank.models import Debit
from bank.decorators import token_required
from bank.serializers import AccountSerializer
from bank.serializers import AccountCreateSerializer
from bank.serializers import BalanceSerializer
from bank.serializers import BalanceUpdateSerializer
from bank.serializers import CreditSerializer
from bank.serializers import DebitSerializer


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


@method_decorator(token_required, name='dispatch')
class AccountView(RetrieveAPIView, CreateAPIView):
    queryset = Account.objects.all()
    lookup_field = 'id'
    
    def get(self, request, user_id, *args, **kwargs):
        self.serializer_class = AccountSerializer
        retrieved = self.retrieve(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=retrieved.data)

    def post(self, request, user_id, *args, **kwargs):
        self.serializer_class = AccountCreateSerializer
        created = self.create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=created.data)


@method_decorator(token_required, name='dispatch')
class BalanceView(RetrieveUpdateAPIView, CreateAPIView):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()
    lookup_field = 'id'
    
    def get(self, request, user_id, *args, **kwargs):
        retrieved = self.retrieve(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=retrieved.data)

    def patch(self, request, user_id, *args, **kwargs):
        self.serializer_class = BalanceUpdateSerializer
        updated = self.partial_update(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=updated.data)

    def post(self, request, user_id, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=created.data)


@method_decorator(token_required, name='dispatch')
class CreditView(CreateAPIView):
    serializer_class = CreditSerializer
    queryset = Credit.objects.all()
    
    def post(self, request, user_id, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=created.data)


@method_decorator(token_required, name='dispatch')
class DebitView(CreateAPIView):
    serializer_class = DebitSerializer
    queryset = Debit.objects.all()
    
    def post(self, request, user_id, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_200_OK, data=created.data)


@method_decorator(token_required, name='dispatch')
class StatementView(APIView):
    def get(self, request, user_id, id, *args, **kwargs):
        credits = CreditSerializer(
            Credit.objects.filter(account_id=id), many=True).data
        debits = DebitSerializer(
            Debit.objects.filter(account_id=id), many=True).data
        return Response(status=status.HTTP_200_OK, data={
            "credits": credits,
            "debits": debits
        })
