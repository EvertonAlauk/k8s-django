from django.contrib import admin
from django.urls import path
from django.urls import include

from core.views import HealthCheck

urlpatterns = [
    path('health/', HealthCheck.as_view(), name='health_check'),
    path('user/', include('core.urls')),
    path('', include('django_prometheus.urls')),
]
