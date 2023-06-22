from .models import *
from rest_framework import serializers


class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sentiment
        fields="__all__"
