from django.urls import path
from django.urls import include

from trade.views import HealthCheck

urlpatterns = [
    path('health/', HealthCheck.as_view(), name='health_check'),
    path('investment/', include('trade.urls')),
    path('', include('django_prometheus.urls')),
]
