from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from .models import Vaga
from .forms import (
    SignUpForm, LoginForm,
    UserUpdateForm, ProfileUpdateForm, VagaForm
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
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    pwd_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
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
                update_session_auth_hash(request, user)
                messages.success(request, "Senha alterada com sucesso!")
                return redirect('login:profile_edit')
            else:
                messages.error(request, "Corrija os erros abaixo para mudar a senha.")

    return render(request, 'login/profile_edit.html', {
        'u_form': u_form,
        'p_form': p_form,
        'pwd_form': pwd_form,
    })
    
def vagas_view(request):
    vagas = Vaga.objects.all()
    
    # Filtros
    busca = request.GET.get('busca', '')
    localizacao = request.GET.get('localizacao', '')
    
    if busca:
        vagas = vagas.filter(title__icontains=busca)
    if localizacao:
        vagas = vagas.filter(location__icontains=localizacao)
    
    # Preparar dados para JavaScript
    vagas_json = []
    for vaga in vagas:
        vagas_json.append({
            'id': vaga.id,
            'title': vaga.title,
            'description': vaga.description,
            'location': vaga.location,
            'salary': vaga.salary or '',
            'requirements': vaga.requirements or '',
            'data_publication': vaga.data_publication.strftime('%d/%m/%Y')
        })
    
    import json
    return render(request, 'login/vagas.html', {
        'vagas': vagas,
        'vagas_json': json.dumps(vagas_json)
    })

@login_required
def conta_view(request):
    """View para exibir informações da conta do usuário"""
    context = {}
    
    if hasattr(request.user, 'profile') and request.user.profile.role == 'RH':
        # Estatísticas para RH
        vagas_criadas = Vaga.objects.filter(created_by=request.user).count()
        vagas_ativas = Vaga.objects.filter(created_by=request.user).count()  # Todas as vagas são ativas por enquanto
        
        context.update({
            'vagas_criadas': vagas_criadas,
            'vagas_ativas': vagas_ativas,
            'candidatos_recebidos': 0,  # Será implementado quando houver sistema de candidaturas
        })
    else:
        # Estatísticas para candidatos
        context.update({
            'candidaturas_enviadas': 0,  # Será implementado quando houver sistema de candidaturas
            'candidaturas_analise': 0,
            'entrevistas_marcadas': 0,
        })
    
    return render(request, 'login/conta.html', context)

@login_required
def candidatos_view(request):
    """View para exibir lista de candidatos (apenas para RH)"""
    # Verificar se o usuário é RH
    if hasattr(request.user, 'profile') and request.user.profile.role == 'RH':
        return render(request, 'login/candidatos.html')
    else:
        messages.error(request, "Acesso negado. Esta página é apenas para RH.")
        return redirect('login:vagas')



@login_required
def adicionar_vaga_view(request):
    """View para adicionar nova vaga (apenas para RH)"""
    if not (hasattr(request.user, 'profile') and request.user.profile.role == 'RH'):
        return JsonResponse({'success': False, 'error': 'Acesso negado'}, status=403)
    
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.created_by = request.user
            vaga.save()
            return JsonResponse({
                'success': True, 
                'message': 'Vaga adicionada com sucesso!',
                'vaga': {
                    'id': vaga.id,
                    'title': vaga.title,
                    'description': vaga.description,
                    'location': vaga.location,
                    'salary': vaga.salary or 'Não informado',
                    'requirements': vaga.requirements or 'Não informado',
                    'data_publication': vaga.data_publication.strftime('%d/%m/%Y')
                }
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)

@login_required
def editar_vaga_view(request, vaga_id):
    """View para editar vaga existente (apenas para RH)"""
    if not (hasattr(request.user, 'profile') and request.user.profile.role == 'RH'):
        return JsonResponse({'success': False, 'error': 'Acesso negado'}, status=403)
    
    vaga = get_object_or_404(Vaga, id=vaga_id)
    
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            vaga = form.save()
            return JsonResponse({
                'success': True, 
                'message': 'Vaga atualizada com sucesso!',
                'vaga': {
                    'id': vaga.id,
                    'title': vaga.title,
                    'description': vaga.description,
                    'location': vaga.location,
                    'salary': vaga.salary or 'Não informado',
                    'requirements': vaga.requirements or 'Não informado',
                    'data_publication': vaga.data_publication.strftime('%d/%m/%Y')
                }
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)

@login_required
def excluir_vaga_view(request, vaga_id):
    """View para excluir vaga (apenas para RH)"""
    if not (hasattr(request.user, 'profile') and request.user.profile.role == 'RH'):
        return JsonResponse({'success': False, 'error': 'Acesso negado'}, status=403)
    
    if request.method == 'POST':
        vaga = get_object_or_404(Vaga, id=vaga_id)
        vaga.delete()
        return JsonResponse({'success': True, 'message': 'Vaga excluída com sucesso!'})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)

@login_required
def obter_vaga_view(request, vaga_id):
    """View para obter dados de uma vaga específica (para edição)"""
    if not (hasattr(request.user, 'profile') and request.user.profile.role == 'RH'):
        return JsonResponse({'success': False, 'error': 'Acesso negado'}, status=403)
    
    vaga = get_object_or_404(Vaga, id=vaga_id)
    return JsonResponse({
        'success': True,
        'vaga': {
            'id': vaga.id,
            'title': vaga.title,
            'description': vaga.description,
            'location': vaga.location,
            'salary': vaga.salary or '',
            'requirements': vaga.requirements or '',
        }
    })

