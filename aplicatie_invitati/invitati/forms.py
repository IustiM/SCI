from django import forms

from invitati.models import Review


class InvitatiForm(forms.Form):
    nume = forms.CharField(max_length=200)
    prenume = forms.CharField(max_length=200)


class CreateReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['titlu', 'corp']
