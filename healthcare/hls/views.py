from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'base.html')


def main(request):
    return render(request, 'main.html', {'title': "Главная"})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {"form": form})


def login(request):
    return render(request, 'login.html')
