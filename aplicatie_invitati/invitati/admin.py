from django.contrib import admin
from .models import Invitati, Review


class InvitatiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nume', 'prenume', 'masa')

admin.site.register(Invitati, InvitatiAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'corp', 'data', 'autor')

admin.site.register(Review, ReviewAdmin)