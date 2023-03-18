from django.urls import path

from .views import homepage, about, mese, review, finish_review

urlpatterns = [
    path('homepage/', homepage),
    path('about/', about),
    path('mese/', mese),
    path('review/', review),
    path('finish-review/', finish_review),
]
