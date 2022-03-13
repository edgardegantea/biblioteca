from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Libro

# Create your views here.
class IndexView(TemplateView):
    model = Libro
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['titulo'] = 'Catálogo de libros'
        context['libros'] = Libro.objects.all()
        return context
