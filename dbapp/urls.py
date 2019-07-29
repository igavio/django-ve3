from django.urls import path
from .views import ArxikiView

urlpatterns = [
    path('', ArxikiView.as_view(), name='arxikiSelida'),
]