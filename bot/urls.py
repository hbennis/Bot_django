from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home, name="accueil"),
    url(r'^reponse/ChatBot', views.view_discussion, name='view_discussion'),
    url(r'^messages/$', views.UserList.as_view()),
]
