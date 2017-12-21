from django.shortcuts import render
from django.http import HttpResponse
from .forms import DiscussionForm, StartForm
from .models import Reponse

from EcpBtBot.MainClass import reponseBot


def home(request):
    instance = Reponse.objects.all()
    instance.delete()

    return render(request, 'bot/accueil.html', locals())

def view_discussion(request):

    form = DiscussionForm(request.POST or None)
    objets = Reponse.objects.all()

    if form.is_valid():
        message = form.cleaned_data['texte']
        envoi = True
        message_sauvegarde = Reponse(reponse = message)
        message_sauvegarde.save()
        repBot = reponseBot(message)
        repBot_sauvegarde = Reponse(reponse=repBot)
        repBot_sauvegarde.save()


        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())