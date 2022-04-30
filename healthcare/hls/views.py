from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('care')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})


def care(request):
    return render(request, 'care.html')
