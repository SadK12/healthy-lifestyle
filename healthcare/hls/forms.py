from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User, Meal, Sport, Starvation


class RegisterUserForm(UserCreationForm):
    name = forms.CharField(max_length=20, required=True, label="Имя", widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "id": "inputName"
    }))
    username = forms.CharField(max_length=20, required=True, label="Никнейм", widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "id": "inputNickname"
    }))
    email = forms.EmailField(max_length=60, required=True, label="Почта", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type": "email",
        "id": "inputEmail",
        "placeholder": "example@example.com"
    }))
    age = forms.IntegerField(required=True, label="Возраст", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputAge"
    }))
    gender = forms.ChoiceField(required=True, label="Пол", choices=[
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ], widget=forms.Select(attrs={
        "class": "form-select",
        "id": "inputGender"
    }))
    height = forms.IntegerField(required=True, label="Рост", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputHeight",
        "placeholder": "см"
    }))
    weight = forms.IntegerField(required=True, label="Вес", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputWeight",
        "placeholder": "кг"
    }))
    activity = forms.ChoiceField(required=True, label="Образ жизни", choices=[
        ('seating', 'Сидячий'),
        ('moderate', 'Умеренный'),
        ('active', 'Активный'),
    ], widget=forms.Select(attrs={
        "class": "form-select",
        "id": "inputActivity"
    }))
    goal = forms.ChoiceField(required=True, label="Цель", choices=[
        ('lose', 'Сбросить вес'),
        ('keep', 'Удержать вес'),
        ('gain', 'Набрать массу'),
    ], widget=forms.Select(attrs={
        "class": "form-select",
        "id": "inputGoal"
    }))
    wrist = forms.IntegerField(required=False, label="Обхват запястья", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputWrist",
        "placeholder": "см"
    }), help_text='Оберните сантиметровую ленту вокруг самой узкой части запястья (необязательное поле)')
    password1 = forms.CharField(required=True, label="Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "inputPassword1"
    }))
    password2 = forms.CharField(required=True, label="Подтвердите пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "inputPassword2"
    }))

    class Meta:
        model = User
        fields = (
            'name',
            'username',
            'email',
            'age',
            'gender',
            'height',
            'weight',
            'activity',
            'goal',
            'wrist',
            'password1',
            'password2'
        )


class LoginUserForm(forms.ModelForm):
    email = forms.CharField(label="Почта", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type": "email",
        "id": "inputEmail"
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "inputPassword"
    }))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Неверно введен логин или пароль")


class AddMealForm(forms.ModelForm):
    category = forms.ChoiceField(label="Категория", choices=[
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
        ('snack', 'Перекус')
    ], widget=forms.Select(attrs={
        "class": "form-control",
        "id": "inputMealCategory"
    }))
    amount = forms.IntegerField(label="Количество (в граммах)", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "id": "inputMealAmount"
    }))

    class Meta:
        model = Meal
        fields = ('category', 'food_name', 'amount')
        widgets = {
            "food_name": forms.Select(attrs={"class": "form-control", "id": "inputMealName"})
        }
        labels = {
            "food_name": "Блюдо"
        }


class AddSportForm(forms.ModelForm):
    duration = forms.IntegerField(label="Длительность (в мин.)", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "id": "inputSportDuration"
    }))

    class Meta:
        model = Sport
        fields = ('activity_type', 'duration')
        widgets = {
            "activity_type": forms.Select(attrs={"class": "form-control", "id": "inputSportType"})
        }
        labels = {
            "activity_type": "Тип активности"
        }


class AddStarvationForm(forms.ModelForm):
    duration = forms.ChoiceField(choices=[
        ('4', '4 часа'),
        ('5', '5 часов'),
        ('6', '6 часов'),
        ('7', '7 часов'),
        ('8', '8 часов')
    ], widget=forms.Select(attrs={
        "class": "form-control",
        "id": "inputStarvationDuration"
    }))

    class Meta:
        model = Starvation
        fields = ('duration',)


class EditUserForm(forms.ModelForm):
    name = forms.CharField(max_length=20, required=True, label="Имя", widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "id": "inputName"
    }))
    username = forms.CharField(max_length=20, required=True, label="Никнейм", widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "id": "inputNickname"
    }))
    email = forms.EmailField(max_length=60, required=True, label="Почта", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type": "email",
        "id": "inputEmail",
        "placeholder": "example@example.com"
    }))
    age = forms.IntegerField(required=True, label="Возраст", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputAge"
    }))
    gender = forms.ChoiceField(required=True, label="Пол", choices=[
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ], widget=forms.Select(attrs={
        "class": "form-select",
        "id": "inputGender"
    }))
    height = forms.IntegerField(required=True, label="Рост", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputHeight",
        "placeholder": "см"
    }))
    weight = forms.IntegerField(required=True, label="Вес", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputWeight",
        "placeholder": "кг"
    }))
    activity = forms.ChoiceField(required=True, label="Образ жизни", choices=[
        ('seating', 'Сидячий'),
        ('moderate', 'Умеренный'),
        ('active', 'Активный'),
    ], widget=forms.Select(attrs={
        "class": "form-select",
        "id": "inputActivity"
    }))
    goal = forms.ChoiceField(required=True, label="Цель", choices=[
        ('lose', 'Сбросить вес'),
        ('keep', 'Удержать вес'),
        ('gain', 'Набрать массу'),
    ], widget=forms.Select(attrs={
        "class": "form-select",
        "id": "inputGoal"
    }))
    wrist = forms.IntegerField(required=False, label="Обхват запястья", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "type": "number",
        "id": "inputWrist",
        "placeholder": "см"
    }), help_text='Оберните сантиметровую ленту вокруг самой узкой части запястья (необязательное поле)')

    class Meta:
        model = User
        fields = (
            'name',
            'username',
            'email',
            'age',
            'gender',
            'height',
            'weight',
            'activity',
            'goal',
            'wrist'
        )
