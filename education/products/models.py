from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    prod_name = models.CharField(max_length=200,
                                 verbose_name='Название продукта',
                                 help_text='Введите название продукта')
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец продукта')
