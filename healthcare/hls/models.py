from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=128)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    goal = models.CharField(max_length=20)
    activity = models.CharField(max_length=20)
    wrist = models.PositiveSmallIntegerField(blank=True, null=True)
    somatotype = models.CharField(max_length=40, null=True)
    consumption_norm = models.PositiveSmallIntegerField(null=True)
    activity_norm = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'


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
