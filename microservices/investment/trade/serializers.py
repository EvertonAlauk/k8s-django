from django.db.models import Sum

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from trade.models import Trade
from trade.decorators import token_required


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'


class TradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        account_id = kwargs['context']['view'].args[0]
        kwargs['data']['account_id'] = account_id
        super().__init__(*args, **kwargs)


class BalanceSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Trade
        fields = [
            'currency',
            'total'
        ]
    
    def get_total(self, obj):
        return Trade.objects.filter(
            account_id=obj.account_id).aggregate(
                Sum('value'))['value__sum']
