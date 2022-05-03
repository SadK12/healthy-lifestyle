from django.contrib import admin

from .models import User, Food, Activity, Meal


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


admin.site.register(User, UserAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Meal, MealAdmin)
