from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class NeoParapono(CreateView):
    model = Parapono
    template_name = 'neo_par.html'
    fields = '__all__'

class TroParapono(UpdateView):
    model = Parapono
    template_name = 'tro_par.html'
    fields = ['katanalotis', 'etairia', 'perigrafi']

class SvyParapono(DeleteView):
    model = Parapono
    template_name = 'svy_par.html'
    #context_object_name = 'svy_parapono'
    