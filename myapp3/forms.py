from django.shortcuts import render
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(max_length=500)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    amount = forms.IntegerField()