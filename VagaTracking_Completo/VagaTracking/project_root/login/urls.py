from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('signup/',  views.signup_view,      name='signup'),
    path('login/',   views.login_view,       name='login'),
    path('logout/',  views.logout_view,      name='logout'),
    path('profile/', views.profile_edit_view, name='profile_edit'),
    path('vagas/', views.vagas_view, name='vagas'),
    path('conta/', views.conta_view, name='conta'),
    path('candidatos/', views.candidatos_view, name='candidatos'),
    
    # URLs para gerenciamento de vagas (RH)
    path('vagas/adicionar/', views.adicionar_vaga_view, name='adicionar_vaga'),
    path('vagas/editar/<int:vaga_id>/', views.editar_vaga_view, name='editar_vaga'),
    path('vagas/excluir/<int:vaga_id>/', views.excluir_vaga_view, name='excluir_vaga'),
    path('vagas/obter/<int:vaga_id>/', views.obter_vaga_view, name='obter_vaga'),
]

