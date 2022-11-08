
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.testview,name="testview"),
path("lowerview",views.lowerview,name="lowerview"),
path("upperi",views.upperi,name="upperi"),
]
