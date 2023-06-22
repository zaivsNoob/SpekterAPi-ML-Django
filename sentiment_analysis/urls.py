from django.urls import path
from .views import analyzer

urlpatterns = [
    path('analyzer/', analyzer),
]