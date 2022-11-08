from django.contrib import admin
from .models import Demoinfo

class Demoi(admin.ModelAdmin):
    list_display = ["name","subject","depart","date"]
# Register your models here.

admin.site.register(Demoinfo,Demoi)
