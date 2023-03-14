from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'price','category_id')
    search_fields = ['name']
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username')
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'user_id', 'deliverdy_date')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'card_id', 'product_id', 'quantity')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Order, OrderAdmin)



