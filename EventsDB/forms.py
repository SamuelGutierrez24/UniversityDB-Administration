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

class UsuarioForm(forms.Form):
    identificacion = forms.CharField(label='Identificador', max_length=100)
    nombres = forms.CharField(label='Nombre Completo', max_length=200)
    tipo_persona_choices = [
        ('Profesor', 'Profesor'),
        ('Estudiante', 'Estudiante'),
        ('Graduado', 'Graduado'),
        ('Empresario', 'Empresario'),
        ('Administrativo', 'Administrativo'),
        ('Directivo', 'Directivo'),
    ]
    tipo_empleado = forms.ChoiceField(label='Tipo de persona', choices=tipo_persona_choices)
    email = forms.EmailField(label='Email')

class CityUserForm(forms.Form):
    ciudad = forms.CharField(label='Ciudad', max_length=100)
    departamento = forms.CharField(label='Departamento', max_length=100)
    pais = forms.CharField(label='País', max_length=100)

class FilterEventForm(forms.Form):
    titulo = forms.CharField(label='Título del evento',max_length=100,widget=forms.TextInput(
        attrs={'placeholder':'Nombre del Evento', 'class': 'inputForm'}
    ))