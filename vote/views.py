from datetime import datetime
from django.shortcuts import render

def choix(request):
    return render(request, 'vote/choix.html', locals())