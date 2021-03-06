from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'shop'

urlpatterns = [
    path('', landingpage, name="home"),
    path('envigoods/', envigoods, name="envigoods"),
    path('serviceintroduce/', serviceintroduce, name="serviceintroduce"),
    path('main/', restaurant_in_category, name='product_all'),
    path('<slug:category_slug>/', restaurant_in_category, name='restaurant_in_category'),
    path('main/<slug:restaurant_slug>/', product_in_restaurant, name='product_in_restaurant'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
    path('sellerPage/register/', ProductRegister.as_view(), name='product_register'),

    path('add/<int:product_id>', add, name='product_add'),
    path('remove/<product_id>', remove, name='product_remove'),
    path('deletecomment/<int:comment_id>', deletecomment, name='deletecomment'),

]
