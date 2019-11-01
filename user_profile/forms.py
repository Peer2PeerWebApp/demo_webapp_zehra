from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#from .models import CustomUser
from register.models import CustomUser

class ViewProfile(UserCreationForm):
    is_tutee = forms.BooleanField(help_text='Select if you want to be a tutee.', required=False)
    is_tutor = forms.BooleanField(help_text='Select if you want to be a tutor.', required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_tutee', 'is_tutor']



'''
class EditProfile(UserCreationForm):
    is_tutee = forms.BooleanField(help_text='Select if you want to be a tutee.', required=False)
    is_tutor = forms.BooleanField(help_text='Select if you want to be a tutor.', required=False)

    class Meta:
        model = CustomUser
        fields = ['is_tutee', 'is_tutor']


    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and CustomUser.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
'''

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_tutee', 'is_tutor']
        exclude = ['password']