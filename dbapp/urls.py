from django.urls import path
from .views import ArxikiView, PeriView, EnaParapono

urlpatterns = [
    path('', ArxikiView.as_view(), name='arxikiSelida'),
    path('peri', PeriView.as_view(), name='periSelida'),
    path('ena_par/<int:pk>/', EnaParapono.as_view(), name='ena_parSelida'),
]