from .forms import DiscussionForm
from .models import Reponse
from django.shortcuts import render
from EcpBtBot.Conversational_Integration import Receiving_Response
from bot.serializers import ReponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import json

def home(request):
    return render(request, 'bot/accueil.html', locals())

def view_discussion(request):
    userid = request.user.id
    #on utilise le field 'username' de la classe User

    form = DiscussionForm(request.POST or None)
    objets = Reponse.objects.filter(name=request.user.username).order_by('created_at')
    if form.is_valid():

        message = form.cleaned_data.get('texte','')
        print(message)
        message_sauvegarde = Reponse(reponse=message, source="user", name=request.user.username)
        message_sauvegarde.save()

        repBot = Receiving_Response(message,userid)

        quickreplies=repBot.quickreplies
        repBot_sauvegarde = Reponse(reponse=repBot.speech, source="bot", name=request.user.username)
        repBot_sauvegarde.save()

        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())


class UserList(APIView):


    def post(self, request, format=None):

        '''POST request to the API returning a dictionary {'success': boolean, 'error': text, 'reponse': bot answer}
        if user is not in the User database, success = False'''

        dico = dict()
        user_name = request.data.get("name", None)
        if not len(list(User.objects.filter(username=user_name))):
            user = User.objects.create_user(request.data['name'], "default", "default")
        else:
            user = User.objects.get(username=user_name)
        message = request.data["reponse"]
        repBot = Receiving_Response(message,user.id)
        #quickreplies = Receiving_Response(message,user.id).quickreplies
        dico["reponse"]=repBot.speech
        dico["quickreplies"]=json.dumps(repBot.quickreplies)
        serializer = ReponseSerializer(data=dico)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


