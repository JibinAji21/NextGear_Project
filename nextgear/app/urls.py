from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('shop_home',views.shop_home),
    path('product_categories/<id>',views.product_categories),


]