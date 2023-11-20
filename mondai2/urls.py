from django.urls import path
from . import views

app_mane='mondai2'
urlpatterns = [
    path('',views.TopView, name="top"),
]     
