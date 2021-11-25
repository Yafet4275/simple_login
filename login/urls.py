#from django.contrib.auth import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login1, name="login"),
    path("home", views.home, name="home"),
    #path("thanks/", views.thanks, name="thanks"),
    #path("checkbox", views.checkbox, name="checkbox"),
]