from django.urls import path
from .views import care, user_settings, statistics, login_user, logout_user, register

urlpatterns = [
    path('', care, name='care'),
    path('care', care, name='care'),
    path('statistics', statistics, name='stats'),
    path('settings', user_settings, name='settings'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]
