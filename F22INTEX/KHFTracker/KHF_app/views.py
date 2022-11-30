from django.shortcuts import render
from .models import recommendation, user, food_item, food_item_in_meal, meal
# Create your views here.

def indexPageView(request):
    recommendations = recommendation.objects.all()
    users = user.objects.all()
    meals = meal.objects.all()
    foods = food_item.objects.all()

    context = {
        'data': recommendations,

        'sexList': (
            ('Male', 'Male'),
            ('Female','Female'),
            ('Other','Other'),
        ),

        'mealList': (
            ('Breakfast', 'Breakfast'),
            ('Lunch', 'Lunch'),
            ('Dinner', 'Dinner'),
            ('Snack', 'Snack'),
            ('Water','Water'),
        ),

        'users': users,
        'meals': meals,
        'foodList' : foods,
    }
    return render(request, 'index.html', context)

def storeUserPageView(request):
    if request.method == 'POST':

        new_user = user()

        #stores the data from each field into the specified spot in the database

        new_user.first_name = request.POST.get('first_name')

        new_user.last_name = request.POST.get('last_name')

        new_user.sex = request.POST.get('sex')

        new_user.height = request.POST.get('height')

        new_user.age = request.POST.get('age')

        new_user.weight = request.POST.get('weight')

        new_user.email = request.POST.get('email')

        new_comorbidity = recommendation.objects.get(comorbidity = request.POST.get('comorbidity'))

        new_user.comorbidity = new_comorbidity

        new_user.save()

    data = user.objects.all()

    context = {
        'users' : data
    }


    return render(request, 'storeUser.html', context)

def storeMealPageView(request):
    if request.method == 'POST':

        new_meal = meal()

        new_meal.date = request.POST.get('date')

        new_meal.notes = request.POST.get('notes')

        new_meal.meal_type = request.POST.get('meal_type')

        new_user = user.objects.get(id = request.POST.get('user'))

        new_meal.user = new_user

        new_meal.save()

    data = meal.objects.all()

    context = {
        'meals' : data,
    }

    return render(request, 'storeMeal.html', context)

def storeFoodInMealPageView(request):
    if request.method == 'POST':
        new_fiin = food_item_in_meal()

        new_food = food_item.objects.get(id = request.POST.get('food_name'))
        new_fiin.food_name = new_food

        new_meal = meal.objects.get(id = request.POST.get('meal'))
        new_fiin.meal = new_meal

        new_fiin.quantity = request.POST.get('quantity')

        new_fiin.save()
    
    data = food_item_in_meal.objects.all()

    context = {
        'fiimList' : data
    }

    return render(request, 'addFood.html', context)


        

def storeFoodPageView(request):

    if request.method == 'POST':
        new_food = food_item()

        new_food.food_name = request.POST.get('food_name')
        
        new_food.measurement_unit = request.POST.get('measurement_unit')

        new_food.save()

    data = food_item.objects.all()

    context = {
        'food_items' : data
    }

    
    return render(request, 'storefood.html', context)


def dataListPageView(request):
    userData = user.objects.all()
    recommendationData = recommendation.objects.all()
    mealData = meal.objects.all()
    food_itemData = food_item.objects.all()




    context = {
        'users' : userData,
        'recommendations' : recommendationData,
        'meals' : mealData,
        'food_items' : food_itemData,

    }
    
    return render(request, 'datalists.html', context)

