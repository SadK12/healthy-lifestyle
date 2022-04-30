from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('care')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {"form": form})


def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('care')

    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('care')

    else:
        form = LoginUserForm()
    return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def care(request):
    return render(request, 'care.html')
