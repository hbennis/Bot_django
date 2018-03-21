from .forms import DiscussionForm
from .models import Discussion, Tokens, Users
from django.shortcuts import render
from EcpBtBot.Conversational_Integration import Receiving_Response
from bot.serializers import ReponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

def home(request):
    return render(request, 'bot/accueil.html', locals())

def view_discussion(request):
    userid = request.user.id
    #on utilise le field 'username' de la classe User

    form = DiscussionForm(request.POST or None)
    #objets = Reponse.objects.filter(name=request.user.username).order_by('created_at')
    objets = Discussion.objects.filter(uid = userid).order_by('created_at')
    if form.is_valid():

        message = form.cleaned_data.get('texte','')
        #message_sauvegarde = Reponse(reponse = message, source = "user", name = request.user.username)
        message_sauvegarde = Discussion(reponse = message, source = "user", name = userid)
        message_sauvegarde.save()

        repBot = Receiving_Response(message,userid)

        quickreplies=repBot.quickreplies
        repBot_sauvegarde = Discussion(reponse=repBot.speech, source = "bot", uid = userid)
        #repBot_sauvegarde = Reponse(reponse=repBot.speech, source = "bot", name = request.user.username)
        repBot_sauvegarde.save()

        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())


class UserList(APIView):


    def post(self, request, format=None):

        '''POST request to the API returning a dictionary {'success': boolean, 'error': text, 'reponse': bot answer}
        if user is not in the User database, success = False'''

        dico = dict()
        userid = request.data.get("id", None)

        if not len(list(User.objects.filter(id=userid))):
            dico["success"] = False
            dico["error"] = 'User not valid'
            dico["reponse"] = 'None'
        else:
            message = request.data["reponse"]
            repBot = Receiving_Response(message,userid).speech
            dico["reponse"]=repBot

        serializer = ReponseSerializer(data=dico)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


