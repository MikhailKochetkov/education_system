from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'prod_name',
        'owner',
    )
    list_editable = ('prod_name', 'owner',)
    search_fields = ('owner',)
    list_filter = ('owner',)
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
