
from django.urls import path

from trade.views import TradeView
from trade.views import BalanceView

urlpatterns = [
    path('trade/<int:id>/', TradeView.as_view(), name='trade_view'),
    path('trade/', TradeView.as_view(), name='trade_view'),
    path('<int:id>/balance/<str:currency>/', BalanceView.as_view(), name='balance_view'),
]
