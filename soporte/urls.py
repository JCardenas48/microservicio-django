from django.urls import path
from django.urls import path
from .views import PQRListCreate, PQRUpdateDelete, PersonaSoporteListCreate, PersonaSoporteUpdateDelete

URLPattern = {
    path('personas-soporte/', PersonaSoporteListCreate.as_view()),
    path('personas-soporte/<pk>/', PersonaSoporteUpdateDelete.as_view()),  
    path('pqr/', PQRListCreate.as_view()),
    path('pqr/<pk>/', PQRUpdateDelete.as_view())
}
