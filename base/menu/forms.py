from cgitb import text
from tkinter.tix import Form
from unicodedata import numeric
from django import forms

class plato_form(forms.Form):
    nombre=forms.CharField(max_length=30)
    descripcion=forms.CharField(max_length=50)
    precio=forms.FloatField()
