
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bank.models import Account
from bank.models import Balance
from bank.models import Credit
from bank.models import Debit


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user_id = kwargs['context']['view'].args[0]
        kwargs['data']['user_id'] = user_id
        super().__init__(*args, **kwargs)

    def validate_user_id(self, user_id):
        if Account.objects.filter(user_id=user_id):
            raise ValidationError('Error exists.')
        return user_id


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        if 'data' in kwargs.keys():
            account_id = kwargs['context']['view'].kwargs['id']
            kwargs['data']['account_id'] = account_id
        super().__init__(*args, **kwargs)

    def validate_account_id(self, account_id):
        if Balance.objects.filter(account_id=account_id):
            raise ValidationError('Balance already exists.')
        return account_id


class BalanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['value']


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        if 'data' in kwargs.keys():
            account_id = kwargs['context']['view'].kwargs['id']
            kwargs['data']['account_id'] = account_id
            value = kwargs['context']['request'].data['value']
            self.change_balance(value, account_id)
        super().__init__(*args, **kwargs)

    def change_balance(self, value, account_id):
        balance = Balance.objects.filter(account_id=account_id).first()
        balance.value += value
        balance.save()


class DebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        if 'data' in kwargs.keys():
            account_id = kwargs['context']['view'].kwargs['id']
            kwargs['data']['account_id'] = account_id
            value = kwargs['context']['request'].data['value']
            self.change_balance(value, account_id)
        super().__init__(*args, **kwargs)

    def change_balance(self, value, account_id):
        balance = Balance.objects.filter(account_id=account_id).first()
        balance.value -= value
        balance.save()

    