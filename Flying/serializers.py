from rest_framework import serializers

from . import models


class AirportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Airport
        fields = ('airportID', 'name', 'city', 'country', 'iata', 'icao',
            'lat', 'lon', 'alt', 'timezone', 'dst', 'tz_db', 'type', 'source')


class AirlineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Airline
        fields = ('airlineID', 'name', 'alias', 'iata', 'icao', 'callsign', 'country', 'active')


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Route
        fields = ('airline', 'airlineID', 'sAirport', 'sAirportID', 
            'dAirport', 'dAirportID', 'codeshare', 'stops', 'equipment')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        fields = ('name', 'iso1', 'iso2', 'campo')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.City 
        fields = ('__all__')


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wish 
        fields = ('__all__')
