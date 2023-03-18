from django.db import models


class Invitati(models.Model):
    nume = models.CharField(max_length=200)
    prenume = models.CharField(max_length=200)
    masa = models.CharField(max_length=200)
    check_in = models.BooleanField(default=False)


class Review(models.Model):
    titlu = models.CharField(max_length=200)
    corp = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Invitati, default=None, on_delete=models.CASCADE)
