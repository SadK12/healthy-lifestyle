from django.urls import path
from .views import login, register, care

urlpatterns = [
    path('', care, name='care'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
