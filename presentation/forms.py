from django import forms

class ContactForm(forms.Form):
    prenom = forms.CharField(max_length=100)
    nom = forms.CharField(max_length=100)
    expediteur = forms.EmailField(label="Votre adresse mail")
    message = forms.CharField(widget=forms.Textarea)
