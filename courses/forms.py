from django import forms


class ViewProfile(UserCreationForm):
    is_tutee = forms.BooleanField(help_text='Select if you want to be a tutee.', required=False)
    is_tutor = forms.BooleanField(help_text='Select if you want to be a tutor.', required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_tutee', 'is_tutor']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_tutee', 'is_tutor']
        exclude = ['password']