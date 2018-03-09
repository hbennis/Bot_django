from .forms import DiscussionForm
from .models import Reponse
from django.shortcuts import render
from EcpBtBot.Conversational_Integration import Receiving_Response


def home(request):
    instance = Reponse.objects.filter(name=request.user.username).all()
    instance.delete()

    return render(request, 'bot/accueil.html', locals())



def view_discussion(request):
    userid = request.user.id
    #on utilise le field 'username' de la classe User

    form = DiscussionForm(request.POST or None)
    objets = Reponse.objects.filter(name=request.user.username).order_by('created_at')
    if form.is_valid():

        message = form.cleaned_data['texte']
        message_sauvegarde = Reponse(reponse = message, source = "user", name = request.user.username)
        message_sauvegarde.save()

        repBot = Receiving_Response(message,userid)

        quickreplies=repBot.quickreplies
        repBot_sauvegarde = Reponse(reponse=repBot.speech, source = "bot", name = request.user.username)
        repBot_sauvegarde.save()

        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())
