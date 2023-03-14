from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.FloatField()
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"
    def get_absolute_url(self):  # new
        return reverse('product')
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    deliverdy_date = models.DateTimeField()
    def __str__(self):
        return str({self.card_id})
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    card_id=models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity=models.FloatField()



    def __str__(self):
        return f"{self.card_id}"

    def get_absolute_url(self):  # new
        return reverse('order')

# Create your models here.
