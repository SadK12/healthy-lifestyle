import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterUserForm, LoginUserForm, AddMealForm
from django.contrib.auth.decorators import login_required
from .models import Food, Meal


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
    user = request.user
    food = Food.objects.all()
    today_date = datetime.date.today()
    tomorrow = today_date + datetime.timedelta(days=1)
    today_meals = Meal.objects.filter(user=request.user).filter(added_at__range=(today_date, tomorrow)).values('category', 'food_name', 'amount')
    k = 0
    eaten_food = [0] * today_meals.count()
    for every_meal in today_meals.iterator():
        temp = food.filter(id=every_meal['food_name']).first()
        eaten_food[k] = {
            'category': every_meal['category'],
            'food_name': temp.name,
            'caloricity': temp.caloricity * (every_meal['amount'] / 100),
            'proteins': round(temp.proteins * (every_meal['amount'] / 100), 2),
            'fats': round(temp.fats * (every_meal['amount'] / 100), 2),
            'carbohydrates': round(temp.carbohydrates * (every_meal['amount'] / 100), 2)
        }
        k += 1
    summed_food = {
        'caloricity': 0,
        'proteins': 0,
        'fats': 0,
        'carbohydrates': 0
    }
    for item in eaten_food:
        summed_food['caloricity'] += item['caloricity']
        summed_food['proteins'] += item['proteins']
        summed_food['fats'] += item['fats']
        summed_food['carbohydrates'] += item['carbohydrates']
    print(summed_food)
    if request.method == 'POST':
        form = AddMealForm(request.POST)
        if form.is_valid:
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
    else:
        form = AddMealForm()
    return render(request, 'care.html', {"user": user, "food": food, "form": form, "summed_food": summed_food})
