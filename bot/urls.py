from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home, name="accueil"),
    url(r'^reponse/(?P<subject>\w+)$', views.view_discussion, name='view_discussion'),
]
