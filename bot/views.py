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
    current_user = Users(user=request.user, connected=True)
    current_user.save()

    form = DiscussionForm(request.POST or None)
    objets = Discussion.objects.filter(uid = request.user.id).order_by('created_at')
    if form.is_valid():

        message = form.cleaned_data.get('texte','')
        message_sauvegarde = Discussion(reponse = message, source = "user", uid = current_user)
        message_sauvegarde.save()

        repBot = Receiving_Response(message,request.user.id)

        quickreplies=repBot.quickreplies
        repBot_sauvegarde = Discussion(reponse=repBot.speech, source = "bot", uid = current_user)
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


