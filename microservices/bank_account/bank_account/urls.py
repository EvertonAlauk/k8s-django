
from django.urls import path
from django.urls import include

from bank.views import HealthCheck

urlpatterns = [
    path('health/', HealthCheck.as_view(), name='health_check'),
    path('bank_account/', include('bank.urls')),
    path('', include('django_prometheus.urls')),
]
