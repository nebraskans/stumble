from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


# Create your views here.


class RenderMap(LoginRequiredMixin, generic.TemplateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'stumble/stumble/main.html'

    def get_context_data(self, **kwargs):
        pass


class CreateAccount(TemplateView):
    template_name = 'stumble/accounts/create-account.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'stumble/accounts/create-account.html', {'form': form})

