from django.urls import path
from .views import index, main, register, login

urlpatterns = [
    path('', index, name='index'),
    path('main/', main, name='main'),
    path('register/', register, name='register'),
    path('login/', login, name='login')
]
