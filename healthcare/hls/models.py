from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, username, email, age, gender, height, weight, goal, activity, password=None):
        if not name:
            raise ValueError("Отсутствует имя пользователя")
        if not email:
            raise ValueError("Отсутствует почта пользователя")
        if not username:
            raise ValueError("Отсутствует никнейм пользователя")
        if not age:
            raise ValueError("Отсутствует возраст пользователя")
        if not gender:
            raise ValueError("Отсутствует пол пользователя")
        if not height:
            raise ValueError("Отсутствует рост пользователя")
        if not weight:
            raise ValueError("Отсутствует вес пользователя")
        if not goal:
            raise ValueError("Отсутствует цель пользователя")
        if not activity:
            raise ValueError("Отсутствует образ жизни пользователя")

        user = self.model(
            name=name,
            username=username,
            email=self.normalize_email(email),
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            goal=goal,
            activity=activity
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, email, age, gender, height, weight, goal, activity, password):
        user = self.create_user(
            name=name,
            username=username,
            email=self.normalize_email(email),
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            goal=goal,
            activity=activity,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(verbose_name='password', max_length=128)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    goal = models.CharField(max_length=20)
    activity = models.CharField(max_length=20)
    wrist = models.PositiveSmallIntegerField(blank=True, null=True)
    somatotype = models.CharField(max_length=40, blank=True, null=True)
    consumption_norm = models.PositiveSmallIntegerField(blank=True, null=True)
    activity_norm = models.PositiveSmallIntegerField(blank=True, null=True)
    BMI = models.PositiveSmallIntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'age', 'gender', 'height', 'weight', 'goal', 'activity']

    objects = UserManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Food(models.Model):
    name = models.CharField(max_length=80)
    caloricity = models.PositiveSmallIntegerField()
    proteins = models.PositiveSmallIntegerField()
    fats = models.PositiveSmallIntegerField()
    carbohydrates = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'


class Activity(models.Model):
    activity_type = models.CharField(max_length=80)
    caloricity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.activity_type

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


class Meal(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    food_name = models.ForeignKey('Food', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)


class Sport(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    activity_type = models.ForeignKey('Activity', on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)


class Starvation(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now=True)
    stopped_at = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
