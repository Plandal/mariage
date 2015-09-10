from datetime import datetime
from django.shortcuts import render
from presentation.forms import ContactForm

def accueil(request):
    return render(request, 'presentation/accueil.html', locals())

def maries(request):
	return render(request, 'presentation/maries.html', locals())

def temoins(request):
	return render(request, 'presentation/temoins.html', locals())

def lieu(request):
	return render(request, 'presentation/lieu.html', locals())

def photos(request):
	return render(request, 'presentation/photos.html', locals())

def contact(request):
	if request.method == 'POST':
			form = ContactForm(request.POST)

			if form.is_valid():

				prenom = form.cleaned_data['prenom']
				nom = form.cleaned_data['nom']
				expediteur = form.cleaned_data['expediteur']
				sujet = form.cleaned_data['sujet']

				# Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

				envoi = True

	return render(request, 'presentation/contact.html', locals())