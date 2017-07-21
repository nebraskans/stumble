from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

class RenderMap(TemplateView):
    template_name = 'stumble/stumble/main.html'


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


class UserProfile(TemplateView):
    template_name = 'stumble/sidebar/user/user.html'