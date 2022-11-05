from django.contrib import admin
from .models import Currency

# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ["name", "symbol", "price", "change", "mcap", "volume", "c_supply"]

admin.site.register(Currency, AppAdmin)