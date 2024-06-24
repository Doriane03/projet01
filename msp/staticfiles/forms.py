from django import forms # type: ignore
class contact_us (forms.Form):
   name=forms.CharField(required=False) 
   email=forms.EmailField()
   message=forms.CharField(max_length=100)
#FORMULAIRE DE MA BASE DE DONNEE
#from django.forms import ModelForm # type: ignore # import pour mon modele form
#from appli_web.models import personnel_soignant# import pour mon modele form
#class personnel_soignantForm(ModelForm):
   #class  Meta:
        #model=personnel_soignant
        #fields=["nom","email","mdp",] #pour afficher tous les champs du model
      
class cnx_form (forms.Form):
   name=forms.CharField(required=True) 
   email=forms.EmailField(required=True)
   password=forms.CharField(max_length=10,widget=forms.PasswordInput,required=True)
#FIN