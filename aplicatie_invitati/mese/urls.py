from django.urls import path

from .views import detalii_mese, check_in

urlpatterns = [
    path('mese/', detalii_mese),
    path('check-in/', check_in),
]
