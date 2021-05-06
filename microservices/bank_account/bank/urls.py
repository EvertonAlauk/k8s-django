
from django.urls import path

from bank import views

urlpatterns = [
    path('account/', views.AccountView.as_view(), name='account_view'),
    path('account/<int:id>/', views.AccountView.as_view(), name='account_view'),
    path('balance/', views.BalanceView.as_view(), name='balance_view'),
    path('balance/<int:id>/', views.BalanceView.as_view(), name='balance_view'),
    path('credit/<int:id>/', views.CreditView.as_view(), name='credit_view'),
    path('debit/<int:id>/', views.DebitView.as_view(), name='debit_view'),
    path('statement/<int:id>/', views.StatementView.as_view(), name='statement_view'),
]
