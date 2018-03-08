from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
import requests
import logging
from django.http import HttpResponse
from django.contrib import auth
from django.template import loader
from .forms import RegisterForm
from bot.models import Reponse
from EcpBtBot.MainClass import *



def index(request):
    try:
        template = loader.get_template('user/index.html')
        user = getFullUserFromRequest(request)
        request.user=user
        return render(request, 'user/index.html', locals())
    except requests.ConnectionError:
        template = loader.get_template('user/error.html')
        return render(request, 'user/error.html', locals())


def getFullUserFromRequest(request):
    if 'user' in request.session._session:
        user = request.session._session['user']  # Dictionnary object with only id and name
        user_id = user['id']
        full_user = User.objects.get(id=user_id)
        return full_user
    else:
        return None


def logIn(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    template = loader.get_template('user/index.html')
    template_error = loader.get_template('user/error.html')
    if user is not None:
        login(request, user)
        dico_users[request.user.id] = {}
        #dès l'authentification, on crée une clé dans le dico_users pour contenir les connexions API de ce user
        logging.info("user authenticated")
        return render(request, 'bot/accueil.html', locals())

    else:
        logging.info("wrong authentication")
        return HttpResponse(template_error.render(request=request))

def logOut(request):
    instance = Reponse.objects.filter(name=request.user.username).all()
    instance.delete()
    auth.logout(request)
    return index(request)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            logging.info(User.objects.filter(username=form.data['username']).exists())
            if User.objects.filter(username=form.data['username']).exists() == False:

                user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
                user.save()
                logging.info(user)
                login(request, user)
                return render(request, 'bot/accueil.html')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'user/register.html', {'form': form})
