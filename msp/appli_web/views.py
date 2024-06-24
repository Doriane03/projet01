from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from appli_web.models  import band # type: ignore
from appli_web.models  import listing  # type: ignore
from appli_web.forms import contact_us # type: ignore
from django.core.mail import send_mail # type: ignore
from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth import  login , logout, authenticate # type: ignore
from django.contrib import messages # type: ignore

#import des class de ma bd
from .models import ordonnancemedicament
from .models import categorielit
from appli_web.models  import antecedant_familial # type: ignore #nouveau
from appli_web.models  import consultation # type: ignore # modifie
from appli_web.models  import antecedant_chirurgical # type: ignore #nouveau
from appli_web.models  import antecedant_medical # type: ignore #nouveau
from appli_web.models  import antecedant_genecologique # type: ignore #nouveau
from appli_web.models  import medicament # type: ignore
from appli_web.models  import categorie # type: ignore
from appli_web.models  import sortie # type: ignore
from appli_web.models  import hospitalisation # type: ignore
from appli_web.models  import service # type: ignore 
from appli_web.models  import chu # type: ignore
from appli_web.models  import pays # type: ignore
from appli_web.models  import type_personnel_soignant # type: ignore
from appli_web.models  import personnel_soignant # type: ignore
from appli_web.models  import facture # type: ignore
from appli_web.models  import constante # type: ignore
from appli_web.models  import patient # type: ignore
from appli_web.models  import lit # type: ignore
from appli_web.models  import ordonnance # type: ignore
from appli_web.models  import diagnostique # type: ignore
from appli_web.models  import bilan_imagerie # type: ignore
from appli_web.models  import bilan_biologique # type: ignore
#finimport

#import formulaire de ma bd
#from appli_web.forms import personnel_soignantForm # type: ignore #pour mon modele from
from appli_web.forms import cnx_form
#fin

# Create your views here.
#def band_list(request):
    #bands=band.objects.all()
    #return HttpResponse(f"""
                        #<ul>
                             #<li>{bands[0].name}</li>
                             #<li>{bands[1].name}</li>
                        #</ul>
#""")
def listing_list(request):
    listings=listing.objects.all()
    return render(request,'appli_web/listing_list.html',context={'listings':listings})

def listing_details(request,id):
    listings=listing.objects.get(id=id)
    return render(request,'appli_web/listing_details.html', context={ 'listings':listings })

def contact(request):
    if request.method =='POST':
        form = contact_us(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['josephinedorianekouadio@gmail.com'],
        )       
    else:
                form=contact_us() 

    return render(request,'appli_web/contact.html',context={'form':form})
#pour ma bd

def connexion(request):
       #form=personnel_soignantForm() #pour afficher un formulaire modele
    
    if  request.method =='POST' :
        if 'connexion' in request.POST:
            email=request.POST['email']
            mdp=request.POST['mdp']
            print(email) 
    return render(request,'appli_web/cnx.html')
#fin
def template(request):
    return render(request,'appli_web/template.html')
def test(request):
    return render(request,'appli_web/template.html')
#fin
def test(request):
    return render(request,'appli_web/template.html')
#fin