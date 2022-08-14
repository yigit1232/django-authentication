
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password/reset/', views.forgot_password, name='forgot_password'),
    path('password/reset/<token>/', views.reset_password, name='reset_password'),
]
