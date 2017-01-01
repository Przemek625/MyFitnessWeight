from django.forms import models
from registration.models import CustomUser
from django import forms


class RegistrationForm(models.ModelForm):
    password = forms.CharField(label='Password', max_length=50)
    password_confirmation = forms.CharField(label='Repeat Password', max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name']

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Password and Repeat Password fields do not match!")

    def save(self, commit=True):
        pass






