from django.views.generic import ListView, TemplateView
from .models import Parapono

class ArxikiView(ListView):
    model = Parapono
    template_name = "arxiki.html"
    context_object_name = "lista_paraponon"

class PeriView(TemplateView):
    template_name = "peri.html"
