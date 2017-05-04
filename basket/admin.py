from django.contrib import admin

from .models import Basket, BasketLine

# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fields = ('status', 'when_created', 'total_price')
    list_display = ('when_created', 'status', 'total_price')
    readonly_fields = ('when_created', 'total_price')


@admin.register(BasketLine)
class BasketLineAdmin(admin.ModelAdmin):
    list_display = ('basket', 'task', 'price')
    readonly_fields = list_display