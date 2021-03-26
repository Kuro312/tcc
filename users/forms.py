from django.forms import ModelForm
from django import forms
from users.models import custom_user


from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
)


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    #input_formats = ['%y-%m-%dT%H:%M']
    # format = '%y-%m-%dT%H:%M'
    pass


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password', 'email',
                  'telefone', 'local', 'data_nascimento']
        widgets = {
            'password': forms.PasswordInput(),
            'data_nascimento': DateInput(format='%Y-%m-%d'),
            # 'username': forms.TextInput(attrs={

            # })
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    permissao = forms.ChoiceField(choices=[(1, 'Aluno'), (2, 'Motorista')])


class UserLoginForm(ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'username': forms.TextInput(attrs={'class': 'username_class'}),
        }


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id"
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
        }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
        }))
