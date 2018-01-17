from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'airports', views.AirportsViewSet)
router.register(r'airlines', views.AirlinesViewSet)
router.register(r'routes', views.RoutesViewSet)
router.register(r'countries', views.CountriesViewSet)
router.register(r'cities', views.CitiesViewSet)
router.register(r'wishes', views.WishesViewSet, base_name='wish')

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    #path('cargar/', views.cargar_base, name='cargar_base'),
    path('deseo/', views.deseo, name='deseo'),
    path('api/', include(router.urls)),
]