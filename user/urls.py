from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.logIn, name='login'),
    url(r'^logout$', views.logOut, name='logOut'),
    url(r'^register$', views.register, name='register'),
]
