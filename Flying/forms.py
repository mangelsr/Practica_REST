from django import forms

from .models import *

class Form(forms.Form):
	paises = Country.objects.all()
	PAISES = []
	for pais in paises:
		tup = pais.name, pais.name
		PAISES.append(tup)
		
	CHOICES = (('directo','Vuelo directo'),('escala','Vuelo con escalas'))
	origen = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)
	destino = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)