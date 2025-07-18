from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role  = forms.ChoiceField(choices=Profile.ROLE_CHOICES, label="Você é:")

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.role = self.cleaned_data['role']
            user.profile.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário ou E‑mail")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['role']


from .models import Vaga

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['title', 'description', 'location', 'salary', 'requirements']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da vaga'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descrição da vaga'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localização'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salário (opcional)'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Requisitos (opcional)'}),
        }

