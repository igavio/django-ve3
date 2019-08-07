from django.urls import path
from .views import ArxikiView, PeriView, EnaParapono, NeoParapono, \
                   TroParapono, SvyParapono

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',                  login_required(ArxikiView.as_view()),  name = 'arxikiSelida'),
    path('peri',              PeriView.as_view(),                    name = 'periSelida'),
    path('ena_par/<int:pk>/', login_required(EnaParapono.as_view()), name = 'ena_parSelida'),
    path('neo_par',           login_required(NeoParapono.as_view()), name = 'neo_parSelida'),
    path('tro_par/<int:pk>/', login_required(TroParapono.as_view()), name = 'tro_parSelida'),
    path('svy_par/<int:pk>/', login_required(SvyParapono.as_view()), name = 'svy_parSelida'),
]
