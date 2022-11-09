
from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("ryan", views.ryan, name="ryan"),
    path("behnaz", views.behnaz, name="behnaz")
]
