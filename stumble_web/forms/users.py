from django import forms
from ..models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegistrationUserForm(forms.Form):
    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label="Username",
        error_messages={'invalid': "This value must contain only letters, numbers and underscores."},

    )

    first_name = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(attrs=dict(required=True, max_length=40)),
        label="First Name",
        error_messages={'invalid': "This value must contain only letters, numbers and underscores."},
    )

    last_name = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(attrs=dict(required=True, max_length=40)),
        label="Last Name",
        error_messages={'invalid': "This value must contain only letters, numbers and underscores."},
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label="Email address"
    )

    password1 = forms.PasswordInput(attrs=dict(required=True, min_length=6, render_value=False))

    password2 = forms.PasswordInput(attrs=dict(required=True, min_length=6, render_value=False,
                                               label="Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegistrationUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'creation_form'
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_account'

        self.helper.add_input(Submit('submit', 'Submit'))
