from django.contrib import admin
from django.urls import path

from core.views import AuthView
from core.views import UserView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='user_auth'),
    path('', UserView.as_view(), name='user_view'),
    path('<int:id>/', UserView.as_view(), name='user_view'),
]
