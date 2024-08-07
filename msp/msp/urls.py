"""

URL configuration for msp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from appli_web import views  # type: ignore
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bands/',views.band_list),
    path('listings/',views.listing_list,name='listing-list'),
    path('listings/<int:id>/',views.listing_details, name='listing-details'),
    path ('contact/',views.contact,name='contact'),
    #pour ma bd
    path ('donne/',views.donne,name='affiche'),
    #fin
    path ('constante/',views.constante,name='constante'),
    path ('patient/',views.patient,name='patient'),
     path ('consultation/',views.consultation,name='consultation'),
    path ('facture/',views.facture,name='facture'),
    #pour ma bd
    path ('connexion/',views.connexion,name='connexion'),
    path ('diagnostique/',views.diagnostique,name='diagnostique'),
    path ('ordonnance/',views.ordonnance,name='ordonnance'),
    
]
