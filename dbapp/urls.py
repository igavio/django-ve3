from django.urls import path
from .views import ArxikiView, PeriView

urlpatterns = [
    path('', ArxikiView.as_view(), name='arxikiSelida'),
    path('peri', PeriView.as_view(), name='periSelida'),
]