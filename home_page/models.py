from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField()
    discount_percent = models.PositiveIntegerField(null=True, blank=True)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount_sold = models.PositiveIntegerField(default=0)


class Order(models.Model):
    total_amount = models.FloatField(null=True, blank=True)
    amount_of_items = models.PositiveIntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def create(cls, products, user):
        order = cls(products=products, user=user)
        order.total_amount = sum([product.price for products in products])
        order.amount_of_items = len(products)
        return order


class UserDetails(models.Model):
    total_amount_spent = models.FloatField()
    total_orders_completed = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
