from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import InvitatiForm, CreateReview
from .models import Invitati


@csrf_exempt
def homepage(request):
    if request.method == "POST":
        return redirect('/pagina1/about')
    return render(request, 'homepage.html')


@csrf_exempt
def about(request):
    if request.method == "POST":
        form = InvitatiForm(request.POST)
        nume = form.data.get('nume')
        prenume = form.data.get('prenume')
        invitat = Invitati.objects.filter(nume=nume, prenume=prenume).first()
        if invitat:
            numarulmesei = invitat.masa
            invitatidelamasa = Invitati.objects.filter(masa=numarulmesei).exclude(nume=nume, prenume=prenume)
            invitat.check_in = True
            invitat.save()
            return render(request, 'about.html', context={
                'form': {'nume': invitat.nume, 'prenume': invitat.prenume, 'masa': numarulmesei,
                         'invitatidelamasa': invitatidelamasa}})
        else:
            return render(request, 'about.html', context={'form': {'eroare': 'persoana nu a fost gasita'}})
    return render(request, 'about.html')


def mese(request):
    return render(request, 'mese.html')


@csrf_exempt
def review(request):
    if request.method == "POST":
        invitat = Invitati.objects.filter(nume=request.POST.get('nume'), prenume=request.POST.get('prenume'))
        if invitat.first():
            return render(request, 'review.html', context={'reviews': invitat})
    return render(request, 'review.html')


@csrf_exempt
def finish_review(request):
    if request.method == "POST":
        invitat = Invitati.objects.filter(nume=request.POST.get('nume'), prenume=request.POST.get('prenume'))
        form = CreateReview(data={'titlu': request.POST.get('titlu'), 'corp': request.POST.get('corp')})
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = invitat.first()
            instance.save()
            return render(request, 'multumim.html')
        else:
            pass
    return render(request, 'review.html')
