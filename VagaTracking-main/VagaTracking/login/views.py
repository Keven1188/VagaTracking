from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm
from django.shortcuts import render
from .models import Vaga

from .forms import (
    SignUpForm, LoginForm,
    UserUpdateForm, ProfileUpdateForm
)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada! Bem-vindo!")
            return redirect('login:vagas')

    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=senha)
            
            if user is not None:
                login(request, user)
                return redirect('login:vagas')
            else:
                messages.error(request, "Senha incorreta.")
        except User.DoesNotExist:
            messages.error(request, "Este e-mail não está cadastrado.")
    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('login:login') 
@login_required
def profile_edit_view(request):
    # instanciar forms vazios para GET
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    pwd_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        # Qual formulário foi submetido?
        if 'update_profile' in request.POST:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, "Perfil atualizado com sucesso!")
                return redirect('login:profile_edit')
        elif 'change_password' in request.POST:
            pwd_form = PasswordChangeForm(request.user, request.POST)
            if pwd_form.is_valid():
                user = pwd_form.save()
                # atualiza sessão para não deslogar
                update_session_auth_hash(request, user)
                messages.success(request, "Senha alterada com sucesso!")
                return redirect('login:profile_edit')
            else:
                # mantém erros para exibir
                messages.error(request, "Corrija os erros abaixo para mudar a senha.")

    return render(request, 'login/profile_edit.html', {
        'u_form': u_form,
        'p_form': p_form,
        'pwd_form': pwd_form,
    })
    
def vagas_view(request):
    return render(request, 'login/vagas.html')

@login_required
def conta_view(request):
    """View para exibir informações da conta do usuário"""
    return render(request, 'login/conta.html')

@login_required
def candidatos_view(request):
    """View para exibir lista de candidatos (apenas para RH)"""
    # Verificar se o usuário é RH
    if hasattr(request.user, 'profile') and request.user.profile.role == 'RH':
        return render(request, 'login/candidatos.html')
    else:
        messages.error(request, "Acesso negado. Esta página é apenas para RH.")
        return redirect('login:vagas')

