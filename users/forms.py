from django.forms import ModelForm
from django import forms
from users.models import custom_user


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
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={})

    permissao = forms.ChoiceField(choices=[(1, 'Aluno'), (2, 'Motorista')])


class UserLoginForm(ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
