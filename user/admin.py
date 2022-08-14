from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,ForgotPassword

@admin.register(ForgotPassword)
class ForgotPasswordAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'token', 'created_at')
    list_filter = ('created_at',)

    class Meta:
        model = ForgotPassword

@admin.register(User)
class Admin(UserAdmin):
    list_display = ('username', 'email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    class Meta:
        model = User


