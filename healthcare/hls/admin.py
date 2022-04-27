from django.contrib import admin

from .models import User, Food, Activity


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'goal', 'activity')
    list_display_links = ('id', 'name')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'caloricity', 'proteins', 'fats', 'carbohydrates')
    list_display_links = ('id', 'name')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_type', 'caloricity')
    list_display_links = ('id', 'activity_type')


admin.site.register(User, UserAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Activity, ActivityAdmin)
