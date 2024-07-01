from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Categoria, Transfer, Chofer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['idVehiculo','patente','cantAsientos','imagen','disponible','categoria','idChofer']
        labels = {
            'idVehiculo': 'Id Vehículo',
            'patente': 'Patente',
            'cantAsientos': 'Cantidad de Asientos',
            'imagen': 'Imagen',
            'disponible': 'Estado',
            'categoria': 'Categoría',
            'idChofer': 'Chofer'
        }
        widgets = {
            'idVehiculo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID del Vehículo',
                    'id': 'idVehiculo'
                }
            ),
            'patente': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Ingrese la Patente',
                        'id': 'patente'
                    }
            ),
            'cantAsientos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la Cantidad de Asientos',
                    'id': 'cantAsientos'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'disponible': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'disponible'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'idChofer': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'idChofer'
                }
            ),
        }

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['idChofer', 'rut', 'dv', 'pNom', 'sNom', 'pApe', 'sApe']
        labels = {
            'idChofer': 'Id Chofer',
            'rut': 'RUT',
            'dv': 'Dígito Verificador',
            'pNom': 'Primer Nombre',
            'sNom': 'Segundo Nombre',
            'pApe': 'Primer Apellido',
            'sApe': 'Segundo Apellido'
        }
        widgets = {
            'idChofer': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID del Chofer',
                    'id': 'idChofer'
                }
            ),
            'rut': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el RUT',
                    'id': 'rut'
                }
            ),
            'dv': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Dígito Verificador',
                    'id': 'dv'
                }
            ),
            'pNom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Primer Nombre',
                    'id': 'pNom'
                }
            ),
            'sNom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Segundo Nombre',
                    'id': 'sNom'
                }
            ),
            'pApe': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Primer Apellido',
                    'id': 'pApe'
                }
            ),
            'sApe': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Segundo Apellido',
                    'id': 'sApe'
                }
            ),
        }

