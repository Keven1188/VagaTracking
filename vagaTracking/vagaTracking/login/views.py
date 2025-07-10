from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import (
    SignUpForm, LoginForm,
    UserUpdateForm, ProfileUpdateForm
)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada! Faça login.")
            return redirect('login:login')
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login:profile_edit')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login:login')

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, "Perfil atualizado.")
                return redirect('login:profile_edit')
        elif 'change_password' in request.POST:
            pwd_form = PasswordChangeForm(request.user, request.POST)
            if pwd_form.is_valid():
                user = pwd_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Senha alterada.")
                return redirect('login:profile_edit')
    else:
        u_form   = UserUpdateForm(instance=request.user)
        p_form   = ProfileUpdateForm(instance=request.user.profile)
        pwd_form = PasswordChangeForm(request.user)

    return render(request, 'login/profile_edit.html', {
        'u_form': u_form, 'p_form': p_form, 'pwd_form': pwd_form
    })
