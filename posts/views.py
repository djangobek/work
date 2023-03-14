from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import *
from .models import *
from django.views.generic.edit import CreateView
class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_new.html'
    fields = ['order_id', 'card_id', 'product_id', 'quantity']
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_editor.html'
    slug_url_kwarg = 'order_id'
    fields = ['card_id', 'product_id', 'quantity']
class ProductCreateView(CreateView): # new
    model = Product
    template_name = 'product_new.html'
    fields = ['product_id', 'name', 'description', 'price','category_id']
class ProductUpdateView(UpdateView): # new
    model = Product
    template_name = 'product_edit.html'
    fields = ['name', 'description', 'price','category_id']
class Home(TemplateView):
    template_name = 'index.html'
class Categorys(ListView):
    model = Category
    template_name = 'category.html'
class Products(ListView):
    model = Product
    template_name = 'product.html'
class Users(ListView):
    model = User
    template_name = 'user.html'
class Cards(ListView):
    model = Card
    template_name = 'card.html'
class Orders(ListView):
    model =Order
    template_name = 'order.html'
class Order_edit(DetailView):
    model = Order
    template_name = 'order_editor.html'
    




