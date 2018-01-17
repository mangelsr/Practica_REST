from django import forms

from .models import *


class Form(forms.Form):
	paises = Country.objects.all()
	PAISES = []
	for pais in paises:
		tup = pais.name, pais.name
		PAISES.append(tup)
		
	origen = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)
	destino = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)


class WishForm(forms.ModelForm):
	class Meta:
		model = Wish
		fields = ['name', 'phone', 'dateI', 'dateF', 'cityI', 'cityF']