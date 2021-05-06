from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from credit.models import Limit
from credit.decorators import token_required


class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = '__all__'


class LimitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        account_id = kwargs['context']['view'].args[0]
        kwargs['data']['account_id'] = account_id
        super().__init__(*args, **kwargs)

    def validate_account_id(self, account_id):
        if Limit.objects.filter(account_id=account_id):
            raise ValidationError('Error exists.')
        return account_id


class LimitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = ['value']
