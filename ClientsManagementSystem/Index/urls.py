from django.urls import path
from . import views

urlpatterns = [
    path('clients-management-system/', views.index, name='index'),
]