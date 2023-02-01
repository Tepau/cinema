
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, PasswordInput

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username',]
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                }),
        }
        labels = {
            'username': "Nom d'utilisateur",
        }
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control',})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', })
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        labels = {
            'username': "Nom d'utilisateur",
        }
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control',})
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control', })
        self.fields['password'].label = "Mot de passe"
        self.fields['username'].label = "Nom d'utilisateur"