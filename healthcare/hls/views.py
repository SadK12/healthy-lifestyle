import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterUserForm, LoginUserForm, AddMealForm, AddSportForm, AddStarvationForm, EditUserForm
from django.contrib.auth.decorators import login_required
from .models import Food, Meal, Activity, Sport, Starvation
from django.utils import timezone


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
    activity = Activity.objects.all()
    today_date = datetime.date.today()
    now_date = timezone.now() + datetime.timedelta(hours=3)
    tomorrow = today_date + datetime.timedelta(days=1)
    today_meals = Meal.objects.filter(user=request.user).filter(added_at__range=(today_date, tomorrow)).values('category', 'food_name', 'amount')
    today_sports = Sport.objects.filter(user=request.user).filter(added_at__range=(today_date, tomorrow)).values('activity_type', 'duration')
    today_starvs = Starvation.objects.filter(user=request.user).filter(started_at__range=(today_date, tomorrow)).values('started_at', 'duration')
    k = 0
    eaten_food = [0] * today_meals.count()
    for every_meal in today_meals.iterator():
        temp = food.filter(id=every_meal['food_name']).first()
        eaten_food[k] = {
            'category': every_meal['category'],
            'food_name': temp.name,
            'caloricity': round(temp.caloricity * (every_meal['amount'] / 100)),
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

    worked_sports = [0] * today_sports.count()
    k = 0
    for every_sport in today_sports.iterator():
        temp_sport = activity.filter(id=every_sport['activity_type']).first()
        worked_sports[k] = {
            'activity_type': temp_sport.activity_type,
            'duration': every_sport['duration'],
            'caloricity': round(temp_sport.caloricity)
        }
        k += 1
    summed_sport = {
        'steps': 0,
        'caloricity': 0
    }
    for item in worked_sports:
        summed_sport['caloricity'] += item['duration'] * item['caloricity']
        if item['activity_type'] == 'ходьба':
            summed_sport['steps'] += item['duration'] * 80
    summed_starv = {
        'is_active': False
    }
    if today_starvs.count() > 0:
        actual_starvs = [0] * today_starvs.count()
        k = 0
        for starv in today_starvs.iterator():
            temp_time = starv['started_at'] + datetime.timedelta(hours=3)
            actual_starvs[k] = {
                'started_at': temp_time,
                'finished_at': temp_time + datetime.timedelta(hours=starv['duration']),
                'duration': starv['duration']
            }
            k += 1
        summed_starv['started_at'] = actual_starvs[-1]['started_at']
        summed_starv['finished_at'] = actual_starvs[-1]['finished_at']
        summed_starv['duration'] = actual_starvs[-1]['duration']
        if (now_date >= summed_starv['started_at']) & (now_date <= summed_starv['finished_at']):
            summed_starv['started_at'] = actual_starvs[-1]['started_at'].strftime("%Y-%m-%dT%H:%M:%S")
            summed_starv['finished_at'] = actual_starvs[-1]['finished_at'].strftime("%Y-%m-%dT%H:%M:%S")
            summed_starv['is_active'] = True
    if request.method == 'POST':
        if 'addMealBtn' in request.POST:
            meal_form = AddMealForm(request.POST)
            if meal_form.is_valid():
                meal = meal_form.save(commit=False)
                meal.user = request.user
                meal.save()
                return redirect('care')
        elif 'addSportBtn' in request.POST:
            sport_form = AddSportForm(request.POST)
            if sport_form.is_valid():
                sport = sport_form.save(commit=False)
                sport.user = request.user
                sport.save()
                return redirect('care')
        elif 'addStarvationBtn' in request.POST:
            starvation_form = AddStarvationForm(request.POST)
            if starvation_form.is_valid():
                starvation = starvation_form.save(commit=False)
                starvation.user = request.user
                starvation.save()
                return redirect('care')
    else:
        meal_form = AddMealForm()
        sport_form = AddSportForm()
        starvation_form = AddStarvationForm()

    context = {
        "user": user,
        "food": food,
        "meal_form": meal_form,
        "sport_form": sport_form,
        "starvation_form": starvation_form,
        "summed_food": summed_food,
        "summed_sport": summed_sport,
        "summed_starv": summed_starv
    }
    return render(request, 'care.html', context)


@login_required
def user_settings(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'settings.html', {"form": form})


@login_required
def statistics(request):
    return render(request, 'stats.html')
