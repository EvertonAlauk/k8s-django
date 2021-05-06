from django.urls import path
from django.urls import include

from credit.views import HealthCheck

urlpatterns = [
    path('health/', HealthCheck.as_view(), name='health_check'),
    path('credit_card/', include('credit.urls')),
    path('', include('django_prometheus.urls')),
]
