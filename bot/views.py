from .forms import DiscussionForm
from .models import Reponse
from django.shortcuts import render
from EcpBtBot.Conversational_Integration import Receiving_Response
from bot.serializers import ReponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

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

        message = form.cleaned_data.get('texte','')
        message_sauvegarde = Reponse(reponse = message, source = "user", name = request.user.username)
        message_sauvegarde.save()

        repBot = Receiving_Response(message,userid)

        quickreplies=repBot.quickreplies
        repBot_sauvegarde = Reponse(reponse=repBot.speech, source = "bot", name = request.user.username)
        repBot_sauvegarde.save()

        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())

class UserList(APIView):

#List all users, or create a new user.

    def get(self, request, format=None):
        messages = Reponse.objects.all()
        serializer = ReponseSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        userid = request.data["id"]
        message = request.data["reponse"]
        repBot = Receiving_Response(message,userid).speech

        dico = dict()
        dico["reponse"]=repBot
        serializer = ReponseSerializer(data=dico)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        reponse = self.get_object(name)
        reponse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(APIView):

#Retrieve, update or delete a user instance.

    def get_object(self, name):
        try:
            return Reponse.objects.filter(name=name)
        except Reponse.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        message = self.get_object(name)
        message = ReponseSerializer(message, many=True)
        return Response(message.data)

    def put(self, request, name, format=None):
        message = self.get_object(name)
        serializer = ReponseSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        message = self.get_object(name)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)