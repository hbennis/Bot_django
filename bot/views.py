from .forms import DiscussionForm
from EcpBtBot.DialogFlow.Config import *
from .models import Response
from django.shortcuts import render
from EcpBtBot.MainClass import *



def home(request):
    instance = Response.objects.filter(name=request.user.username).all()
    instance.delete()

    return render(request, 'bot/accueil.html', locals())



def view_discussion(request, subject):
    userid = request.user.id
    #on utilise le field 'username' de la classe User
    if subject not in dico_users[userid]:
        dico_users[userid][subject] = API_Response(subject)
        #si l'utilisateur n'a jamais choisi ce thème, ouvrir une connexion API correspondante
    connexion = dico_users[userid][subject]


    form = DiscussionForm(request.POST or None)
    objets = Response.objects.filter(name=request.user.username).order_by('created_at')
    #quickreplies
    if form.is_valid():

        message = form.cleaned_data['texte']
        #envoi = True
        message_sauvegarde = Response(Response = message, source = "user", name = request.user.username)
        message_sauvegarde.save()
        repBot = connexion.ResponseBot(message)

        intent = repBot.intent
        
        if intent in tokens:
            subject = intent
        if intent.upper() == "AU REVOIR":
            subject= "intro"

        quickreplies=repBot.quickreplies
        repBot_sauvegarde = Response(Response=repBot.speech, source = "bot", name = request.user.username)
        repBot_sauvegarde.save()

        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())
