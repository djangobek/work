
from django.urls import path
from 
from .views import *

urlpatterns = [

    path('order/new/', OrderCreateView.as_view(), name='order_new'),
    path('order/edit/', OrderUpdateView.as_view(), name='order_edit'),
    path('product/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/new/', ProductCreateView.as_view(), name='product_new'),
    path('', Home.as_view(), name='index'),
    path('category/',Categorys.as_view(), name='category'),
    path('product/',Products.as_view(), name='product'),
    path('user/',Users.as_view(), name='user'),
    path('card/',Cards.as_view(), name='card'),
    path('order/',Orders.as_view(), name='order'),
    path('order/<int:pk>/', Order_edit.as_view(), name="myfive")
    
]