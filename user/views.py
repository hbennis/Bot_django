import logging
import requests
from bot.models import Discussion, Users_bdd
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.template import loader
from EcpBtBot.MainClass import *
from .forms import RegisterForm
from EcpBtBot.Conversational_Integration import *

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
        user.save()
        user.users_bdd.connected = True
        logging.info("user authenticated")
        return render(request, 'bot/accueil.html', locals())

    else:
        logging.info("wrong authentication")
        return HttpResponse(template_error.render(request=request))

def logOut(request):
    instance = Discussion.objects.filter(uid=request.user.id).all()
    instance.delete()
    ##to-do: ne plus supprimer toutes les discussions
    users_agents.removeDisconnectedMember(request.user.id)
    request.user.users_bdd.connected = False
    request.user.users_bdd.current_subject = 'intro'
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
                user_bdd = Users_bdd(user = user, connected = False, current_subject = 'intro')
                user_bdd.save()
                logging.info(user)
                login(request, user)
                return render(request, 'bot/accueil.html')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'user/register.html', {'form': form})
