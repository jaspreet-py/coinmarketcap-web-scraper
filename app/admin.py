from django.contrib import admin
from .models import Currency

# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ["id", "source", "updated_on", "data"]

admin.site.register(Currency, AppAdmin)