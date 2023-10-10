from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    prod_name = models.CharField(max_length=200,
                                 verbose_name='Название продукта',
                                 help_text='Введите название продукта')
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец продукта')


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accesses')
    is_valid = models.BooleanField(default=True)
