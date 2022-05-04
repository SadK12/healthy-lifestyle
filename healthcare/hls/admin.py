from django.contrib import admin

from .models import User, Food, Activity, Meal, Sport, Starvation


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'height', 'weight', 'goal', 'activity')
    list_display_links = ('id', 'name')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'caloricity', 'proteins', 'fats', 'carbohydrates')
    list_display_links = ('id', 'name')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_type', 'caloricity')
    list_display_links = ('id', 'activity_type')


class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'food_name', 'amount', 'added_at')
    list_display_links = ('category', 'food_name')


class SportAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration', 'added_at')
    list_display_links = ('user', 'activity_type', 'duration', 'added_at')


class StarvationAdmin(admin.ModelAdmin):
    list_display = ('user', 'started_at', 'duration')
    list_display_links = ('user', 'started_at', 'duration')


admin.site.register(User, UserAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Starvation, StarvationAdmin)
