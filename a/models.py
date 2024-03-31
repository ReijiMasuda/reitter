from django.db import models

class Tweet(models.Model):
    message = models.CharField(max_length=40)
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True) 
