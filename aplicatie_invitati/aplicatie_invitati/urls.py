from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina1/', include('invitati.urls')),
    path('pagina2/', include('mese.urls')),
]
