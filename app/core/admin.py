from django.contrib import admin
from .models import Libro, Autor, Categoria, Editorial

# Register your models here.
# admin.site.register(Libro)
# admin.site.register(Autor)
# admin.site.register(Categoria)
# admin.site.register(Editorial)

#@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('editorial', 'autor', 'titulo', 'sinopsis')
    list_filter = ('editorial', 'autor')
    fields = [('editorial', 'autor'), 'titulo', 'portada', 'sinopsis']

admin.site.register(Libro, LibroAdmin)


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'alias', 'fechaNacimiento')

admin.site.register(Autor, AutorAdmin)
