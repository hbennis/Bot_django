from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
import requests
from django.http import HttpResponse
from django.contrib import auth
from django.template import loader
from .forms import RegisterForm


def index(request):
    try:
        template = loader.get_template('user/index.html')
        user = getFullUserFromRequest(request)
        request.user=user
        return HttpResponse(template.render(request=request))
    except requests.ConnectionError:
        template = loader.get_template('user/error.html')
        return HttpResponse(template.render(request=request))


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
        print("user authenticated")
        return HttpResponse(template.render(request=request))
    else:
        print("wrong authentication")
        return HttpResponse(template_error.render(request=request))

def logOut(request):
    auth.logout(request)
    return index(request)


def home(request):
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.data['username']).exists() == False:

                user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
                user.save()
                print(user)
            login(request, user)
            return render(request, 'user/index.html')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'user/register.html', {'form': form})

