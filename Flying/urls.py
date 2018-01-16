from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'airports', views.AirportsViewSet)
router.register(r'airlines', views.AirlinesViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('cargar/', views.cargar_base, name='cargar_base'),
    path('api/', include(router.urls)),
]