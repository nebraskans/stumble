from django import forms
from ..models import User


class RegistrationUserForm(forms.Form):
    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label=_("Username"),
        error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")},
        attrs={'class':'form-field'},

    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label=_("Email address"),
        attrs={'class':'form-field'},
    )

    password1 = forms.PasswordInput(attrs=dict(required=True, min_length=6, render_value=False), attrs={'class':'form-field'})

    password2 = forms.PasswordInput(attrs=dict(required=True, min_length=6, render_value=False,
                                               label=_("Password (again)"))attrs={'class':'form-field'})

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data