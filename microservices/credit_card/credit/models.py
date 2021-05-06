from django.db import models

class Limit(models.Model):
    
    account_id = models.PositiveIntegerField('Id do usuário', null=False)
    value = models.FloatField('Valor', default=1000.0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = 'Limit'
        verbose_name_plural = 'Limits'
        db_table = 'limits'

    def __str__(self):
        return f'Conta do usuário: #{self.user_id} - {self.value}'