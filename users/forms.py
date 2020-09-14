from django.forms import ModelForm
from django import forms
from users.models import custom_user


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    #input_formats = ['%y-%m-%dT%H:%M']
    # format = '%y-%m-%dT%H:%M'
    pass


class UserForm(ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password',
                  'date_joined', 'telefone', 'local']
        widgets = {
            'password': forms.PasswordInput(),
            'date_joined': DateTimeInput(format='%Y-%m-%dT%H:%M'),
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
        }
