from django.contrib import admin

from .models import Basket, BasketLine

# Register your models here.

admin.site.register(Basket)
admin.site.register(BasketLine)
