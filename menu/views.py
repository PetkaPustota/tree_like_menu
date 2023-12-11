import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView
from menu.models import Menu


# view главной страницы с меню

class FirstView(TemplateView):
    model = Menu
    template_name = "index.html"


# view для страницы объекта с поиском по slug

class ObjectDetailView(DetailView):
    model = Menu
    template_name = "detail.html"
