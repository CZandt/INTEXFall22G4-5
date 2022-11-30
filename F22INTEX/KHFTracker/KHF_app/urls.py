from django.urls import path
from .views import indexPageView,storeUserPageView, dataListPageView, storeFoodPageView, storeMealPageView, storeFoodInMealPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('users', storeUserPageView, name='storeuser'),
    path('datalist', dataListPageView, name='dataList'),
    path('storeFood', storeFoodPageView, name='storefood'),
    path('storeMeal', storeMealPageView, name='storeMeal'),
    path('addFood', storeFoodInMealPageView, name='addFood'),
]

