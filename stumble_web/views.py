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
from .forms.users import RegistrationUserForm
from django.views.generic import FormView
from django.http import HttpResponseRedirect

# Create your views here.


class RenderMap(LoginRequiredMixin, generic.TemplateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'stumble/stumble/main.html'

    def get_context_data(self, **kwargs):
        pass


class CreateAccount(FormView):
    template_name = 'stumble/accounts/create-account.html'
    form_class = RegistrationUserForm
    success_url = '/home/'

    def post(self, request, *args, **kwargs):
        create_account_form = self.form_class(request.POST, request)

        if create_account_form.is_valid():
            cleaned_data = create_account_form.cleaned_data
            first_name = cleaned_data['first_name']
            last_name = cleaned_data['last_name']
            username = cleaned_data['username']
            password = cleaned_data['username']
            User.objects.create(first_name=first_name, last_name=last_name, username=username, password=password)
            authenticate(username=username, password=password)
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/')




# class GeneralHealthFormView(LoginRequiredMixin, FormView):
#     """ Handles general health view for a patient, and form """
#     form_class = GeneralHealthForm
#     template_name = 'healthnetapp/manage/patient.html'
#     success_url = '/'
#
#     def post(self, request, *args, **kwargs):
#         general_health_form = self.form_class(request.POST, request=request)
#         patient = Patient.objects.get(pk=kwargs.pop('pk'))
#
#         if general_health_form.is_valid():
#             cleaned_data = general_health_form.cleaned_data
#             patient.primary_language = cleaned_data['primary_language']
#             patient.ethnicity = cleaned_data['ethnicity']
#             # if cleaned_data['height'] != 'N/A':
#             patient.height = int(cleaned_data['height'])
#             # if cleaned_data['weight'] != 'N/A':
#             patient.weight = int(cleaned_data['weight'])
#             patient.smoke = cleaned_data['smoke']
#             patient.drink = cleaned_data['drink']
#             patient.drugs = cleaned_data['drugs']
#             patient.save()
#             messages.success(request, 'Updated patient health info')
#             return HttpResponseRedirect('/manage/patients/view/%s/' % patient.pk)
#         else:
#             messages.error(request, 'An error has occurred')
#             return HttpResponseRedirect('/manage/patients/view/%s/' % patient.pk)
#

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

