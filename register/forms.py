from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    is_tutee = forms.BooleanField(help_text='Select if you want to be a tutee.', required=False)
    is_tutor = forms.BooleanField(help_text='Select if you want to be a tutor.', required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_tutee', 'is_tutor']