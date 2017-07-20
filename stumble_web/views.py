from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class RenderMap(TemplateView):
    template_name = 'stumble/stumble/main.html'


class CreateAccount(TemplateView):
    template_name = 'stumble/accounts/create-account.html'

