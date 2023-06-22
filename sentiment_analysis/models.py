from django.db import models

# Create your models here.

class Sentiment(models.Model):
    name=models.CharField(max_length=20)
    message=models.TextField()
    