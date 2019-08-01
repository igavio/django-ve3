from django.views.generic \
    import ListView, TemplateView, DetailView
from .models import Parapono

class ArxikiView(ListView):
    model = Parapono
    template_name = 'arxiki.html'
    context_object_name = 'lista_paraponon'

class PeriView(TemplateView):
    template_name = 'peri.html'

class EnaParapono(DetailView):
    model = Parapono
    template_name = 'ena_par.html'
    context_object_name = 'ena_parapono'
