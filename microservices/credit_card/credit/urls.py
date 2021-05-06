
from django.urls import path

from credit.views import LimitView

urlpatterns = [
    path('limit/<int:id>/', LimitView.as_view(), name='limit_view'),
    path('limit/', LimitView.as_view(), name='limit_view'),
]
