from django.db import models


class Account(models.Model):
    
    user_id = models.PositiveIntegerField('Id do usuário', null=False)
    active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        db_table = 'accounts'

    def __str__(self):
        return f'Conta do usuário: #{self.user_id}'


class Balance(models.Model):
    
    account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    value = models.FloatField('Valor', default=0.0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        db_table = 'balances'

    def __str__(self):
        return f'Conta do usuário: #{self.account_id.user_id} - saldo: {self.value}'


class Credit(models.Model):
    
    account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    value = models.FloatField('Valor', default=0.0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Credit'
        verbose_name_plural = 'Credits'
        db_table = 'credits'

    def __str__(self):
        return f'Conta do usuário: #{self.account_id.user_id} - crédito: {self.value}'


class Debit(models.Model):
    
    account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    value = models.FloatField('Valor', default=0.0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Debit'
        verbose_name_plural = 'Debits'
        db_table = 'debits'

    def __str__(self):
        return f'Conta do usuário: #{self.account_id.user_id} - débito: {self.value}'

