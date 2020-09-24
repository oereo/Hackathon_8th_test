from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'shop'

urlpatterns = [
    path('', landingPage, name="home"),
    path('main/', restaurant_in_category, name='product_all'),
    path('<slug:category_slug>/', restaurant_in_category, name='restaurant_in_category'),
    path('main/<slug:restaurant_slug>/', product_in_restaurant, name='product_in_restaurant'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]