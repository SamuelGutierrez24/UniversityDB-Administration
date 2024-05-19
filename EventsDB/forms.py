# En el archivo forms.py de tu aplicación Django

from django import forms

# Define un formulario para el registro de eventos
class EventForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    CATEGORIAS_CHOICES = [
        ('Informativo', 'Informativo'),
        ('Taller', 'Taller'),
        ('Innovación', 'Innovación'),
        ('Modificaciones', 'Modificaciones'),
    ]
    categoria = forms.ChoiceField(label='Categoría', choices=CATEGORIAS_CHOICES)
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))

class EventPlaceForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=200)
    ciudad = forms.CharField(label='Ciudad', max_length=100)

