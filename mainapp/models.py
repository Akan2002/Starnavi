from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    def __str__(self) -> str:
        return self.user
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class SmsUser(models.Model):
    Sms = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='smss')
    message = models.TextField(default=0)

    def __str__(self) -> str:
        return self.user.username
    class Meta:
        verbose_name = 'Sms'
        verbose_name_plural = verbose_name + 's' 

