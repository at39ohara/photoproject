from django.urls import path
from . import views

app_name = 'kokura'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'kokura'),

     # コンタクトカテゴリの
    path('contact/', views.ContactView.as_view(), name = 'contact'),
]