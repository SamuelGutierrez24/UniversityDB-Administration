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
    identificador = forms.CharField(label='Identificador', max_length=100)
    nombre_usuario = forms.CharField(label='Nombre de Usuario', max_length=100)
    nombre_completo = forms.CharField(label='Nombre Completo', max_length=200)
    TIPO_RELACION_CHOICES = [
        ('Profesor', 'Profesor'),
        ('Estudiante', 'Estudiante'),
        ('Graduado', 'Graduado'),
        ('Empresario', 'Empresario'),
        ('Administrativo', 'Administrativo'),
        ('Directivo', 'Directivo'),
        # Agrega más opciones según sea necesario
    ]
    tipo_relacion = forms.ChoiceField(label='Tipo de Relación', choices=TIPO_RELACION_CHOICES)
    email = forms.EmailField(label='Email')