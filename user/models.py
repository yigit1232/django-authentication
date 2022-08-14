from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_name = None
    first_name = None
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table='users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class ForgotPassword(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_id')
    token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='forgot_password'
        verbose_name = 'Forgot Password'
        verbose_name_plural = 'Forgot Passwords'

    def __str__(self):
        return self.user_id.username