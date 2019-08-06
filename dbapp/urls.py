from django.urls import path
from .views import ArxikiView, PeriView, EnaParapono, NeoParapono, \
                   TroParapono, SvyParapono

urlpatterns = [
    path('',                  ArxikiView.as_view(),  name = 'arxikiSelida'),
    path('peri',              PeriView.as_view(),    name = 'periSelida'),
    path('ena_par/<int:pk>/', EnaParapono.as_view(), name = 'ena_parSelida'),
    path('neo_par',           NeoParapono.as_view(), name = 'neo_parSelida'),
    path('tro_par/<int:pk>/', TroParapono.as_view(), name = 'tro_parSelida'),
    path('svy_par/<int:pk>/', SvyParapono.as_view(), name = 'svy_parSelida'),
]
