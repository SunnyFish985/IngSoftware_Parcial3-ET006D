from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Categoria, Transfer, Chofer, DetalleTicket, Ticket

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

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['pNomP', 'pApeP', 'rut']
        labels = {
            'pNomP': 'Primer Nombre',
            'pApeP': 'Primer Apellido',
            'rut': 'RUT',
        }
        widgets = {
            'pNomP': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su primer nombre',
                    'id': 'pNomP'
                }
            ),
            'pApeP': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su primer apellido',
                    'id': 'pApeP'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su RUT',
                    'id': 'rut'
                }
            ),
        }

class DetalleForm(forms.ModelForm):
    class Meta:
        model = DetalleTicket
        fields = ['transfer', 'destino', 'asientosReserva']
        labels = {
            'transfer': 'Transfer',
            'destino': 'Destino',
            'asientosReserva': 'Cantidad de Asientos',
        }
        widgets = {
            'transfer': forms.Select(attrs={'class': 'form-control', 'id': 'transfer'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su destino', 'id': 'destino'}),
            'asientosReserva': forms.NumberInput(attrs={'class': 'form-control', 'id': 'asientosReserva'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['transfer'].queryset = Transfer.objects.filter(disponible=True)

        if 'transfer' in self.data:
            try:
                transfer_id = int(self.data.get('transfer'))
                transfer = Transfer.objects.get(idVehiculo=transfer_id)
                self.fields['asientosReserva'].widget.attrs['max'] = transfer.cantAsientos
            except (ValueError, TypeError, Transfer.DoesNotExist):
                pass
        elif self.instance.pk:
            self.fields['asientosReserva'].widget.attrs['max'] = self.instance.transfer.cantAsientos

