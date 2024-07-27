from django.contrib import admin
from .models import Vegetables

class VgetablesAdmin(admin.ModelAdmin):
    list_display = ("name","price","quantity")

admin.site.register(Vegetables, VgetablesAdmin)