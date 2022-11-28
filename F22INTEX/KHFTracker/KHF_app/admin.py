from django.contrib import admin
from .models import recommendation, user, meal, food_item, food_item_in_meal
# Register your models here.
admin.site.register(recommendation)
admin.site.register(user)
admin.site.register(meal)
admin.site.register(food_item)
admin.site.register(food_item_in_meal)