from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersListView(ListView):
    model = User
    template_name = 'users.html'