from .forms import DiscussionForm
from .models import Reponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from EcpBtBot.MainClass import *
from django.http import HttpResponse
from user.views import logIn



def home(request):
    instance = Reponse.objects.filter(name=request.user.username).all()
    instance.delete()

    return render(request, 'bot/accueil.html', locals())

def view_discussion(request, sujet):
    user = request.user.username
    #on utilise le field 'username' de la classe User
    if sujet not in dico_users[user]:
        dico_users[user][sujet] = API_reponse(sujet)
        #si l'utilisateur n'a jamais choisi ce thème, ouvrir une connexion API correspondante

    connexion = dico_users[user][sujet]

    form = DiscussionForm(request.POST or None)
    objets = Reponse.objects.filter(name=request.user.username).order_by('created_at')

    if form.is_valid():

        message = form.cleaned_data['texte']
        envoi = True
        message_sauvegarde = Reponse(reponse = message, source = "user", name = request.user.username)
        message_sauvegarde.save()
        repBot = connexion.reponseBot(message)
        repBot_sauvegarde = Reponse(reponse=repBot, source = "bot", name = request.user.username)
        repBot_sauvegarde.save()


        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())
