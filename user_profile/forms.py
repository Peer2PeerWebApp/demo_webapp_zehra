from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#from .models import CustomUser
from register.models import CustomUser

class ViewProfile(UserCreationForm):
    #full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    is_tutee = forms.BooleanField(help_text='Select if you want to be a tutee.')
    is_tutor = forms.BooleanField(help_text='Select if you want to be a tutor.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_tutee', 'is_tutor']