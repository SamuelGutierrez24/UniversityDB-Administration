# En el archivo forms.py de tu aplicación Django

from django import forms
from .models import *

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
    facultad = forms.ModelChoiceField(queryset=facultades.objects.all(), label='Facultad organizadora')


class EventPlaceForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=200)
    ciudad = forms.CharField(label='Ciudad', max_length=100)

class UsuarioForm(forms.Form):
    identificacion = forms.CharField(label='Identificador', max_length=100)
    nombres = forms.CharField(label='Nombre Completo', max_length=200)
    tipo_persona_choices = [
        ('DOCENTE', 'DOCENTE'),
        ('Estudiante', 'Estudiante'),
        ('Graduado', 'Graduado'),
        ('Empresario', 'Empresario'),
        ('ADMINISTRATIVO', 'ADMINISTRATIVO'),
        ('Directivo', 'Directivo'),
    ]
    tipo_empleado = forms.ChoiceField(label='Tipo de persona', choices=tipo_persona_choices)
    email = forms.EmailField(label='Email')

class CityUserForm(forms.Form):
    ciudad = forms.CharField(label='Ciudad', max_length=100)
    departamento = forms.CharField(label='Departamento', max_length=100)
    pais = forms.CharField(label='País', max_length=100)

class CommentsForm(forms.Form):
    idPerson = forms.CharField(label='Ingrese la identificación de la persona',required=True,widget=forms.TextInput(
        attrs={'placeholder': 'Identificación Persona','name':'idPerson'}
    ))
    idEvent = forms.CharField(label='Ingrese el nombre del evento',required=True,widget=forms.TextInput(
        attrs={'placeholder' : 'Nombre Evento','name':'idEvent'}
    ))
    comment = forms.CharField(label='Comentarios sobre el evento',required=True,widget=forms.Textarea(
        attrs={'placeholder' : 'Escribe tu comentario aquí...', 'name' : 'comment'}
    ))

class FilterEventsForm(forms.Form):
    CATEGORIAS_CHOICES = [
        ('Informativo', 'Informativo'),
        ('Taller', 'Taller'),
        ('Innovación', 'Innovación'),
        ('Modificaciones', 'Modificaciones'),
    ]
    categoria = forms.ChoiceField(label='Categoría', choices=CATEGORIAS_CHOICES)