from distutils.command.upload import upload
from enum import unique
from tabnanny import verbose
from django.db import models
from django.forms import URLField

# CATEGORIAS_LIBRO = (('cat01', 'Terror'), ('cat02', 'Novela'), ('cat03', 'Relatos'))

class Autor(models.Model):
    nombre = models.CharField(verbose_name='Nombre del Autor', max_length=50)
    apellidos = models.CharField(verbose_name='Apellido (s)', max_length=80)
    alias = models.CharField(verbose_name='Alias', max_length=50, null=True)
    fechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    fechaFallecimiento = models.DateField(verbose_name='Fecha de fallecimiento', blank=True, null=True)
    foto = models.ImageField(verbose_name='Foto del autor', upload_to='imagenes/autores/', null=True)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidos)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Editorial(models.Model):
    nombre = models.CharField(verbose_name='Editorial', max_length=100, unique=True)
    email = models.EmailField(verbose_name='Correo electrónico', max_length=100, unique=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=15, null=True)
    url = models.URLField(verbose_name='URL de la Editorial', max_length=255, null=True)
    pais = models.CharField(verbose_name='País', max_length=50)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la categoría', max_length=50, unique=True)
    descripcion = models.TextField(verbose_name='Descripción', max_length=1000)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, verbose_name='Elija la Editorial')
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, verbose_name='Seleccione el autor')
    titulo = models.CharField(verbose_name='Título del libro', max_length=150)
    categoria = models.ManyToManyField(Categoria, verbose_name='Seleccione la(s) categoría(s)')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    portada = models.ImageField(verbose_name='Portada', upload_to='imagenes/libros/', null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'
    