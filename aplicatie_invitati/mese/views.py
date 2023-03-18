from django.shortcuts import render

from invitati.models import Invitati


def detalii_mese(request):
    if request.method == 'GET':
        mese = Invitati.objects.all().values('masa')
        return render(request, 'mese.html', context={'mese': mese})


def check_in(request):
    if request.method == 'GET':
        check_in = Invitati.objects.filter(check_in=True)
        return render(request, 'check_in.html', context={'check_in': check_in})
