# VagaTracking - Sistema de Gerenciamento de Vagas

## Descrição
Sistema web desenvolvido em Django para gerenciamento de vagas de emprego, permitindo que usuários RH publiquem vagas e candidatos visualizem oportunidades disponíveis.

## Funcionalidades Implementadas

### ✅ Sistema de Autenticação
- Login e cadastro de usuários
- Perfis diferenciados (Candidato/RH)
- Proteção CSRF configurada para acesso externo

### ✅ Gerenciamento de Vagas (RH)
- Adicionar novas vagas via modal/pop-up
- Editar vagas existentes
- Excluir vagas
- Visualizar lista de vagas criadas

### ✅ Visualização de Vagas (Candidatos)
- Lista de todas as vagas disponíveis
- Filtros por título e localização
- Detalhes completos das vagas
- Interface responsiva

### ✅ Página de Conta
- Informações pessoais do usuário
- Estatísticas em tempo real:
  - Vagas criadas (para RH)
  - Candidatos recebidos
  - Vagas ativas
- Ações rápidas para navegação
- Histórico de atividades recentes

## Estrutura do Projeto

```
VagaTracking/
├── project/
│   ├── settings.py          # Configurações do Django
│   ├── urls.py             # URLs principais
│   └── wsgi.py
├── login/
│   ├── models.py           # Modelos (User, Profile, Vaga)
│   ├── views.py            # Views do sistema
│   ├── forms.py            # Formulários
│   ├── urls.py             # URLs do app
│   └── templates/login/    # Templates HTML
├── static/
│   └── css/               # Arquivos CSS
└── manage.py
```

## Modelos de Dados

### Profile
- `user`: Relacionamento com User do Django
- `role`: Tipo de usuário ('Candidato' ou 'RH')
- `created_at`: Data de criação

### Vaga
- `titulo`: Título da vaga
- `localizacao`: Localização da vaga
- `salario`: Faixa salarial (opcional)
- `descricao`: Descrição detalhada
- `requisitos`: Requisitos da vaga (opcional)
- `created_by`: Usuário que criou a vaga
- `created_at`: Data de criação
- `is_active`: Status da vaga

## Como Executar

1. **Instalar dependências:**
   ```bash
   pip install django
   ```

2. **Aplicar migrações:**
   ```bash
   python manage.py migrate
   ```

3. **Criar superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

4. **Executar servidor:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Usuários de Teste

### Usuário RH
- **Email:** rh@test.com
- **Senha:** rh123
- **Tipo:** Recursos Humanos

### Superusuário
- **Username:** admin
- **Email:** admin@test.com
- **Senha:** admin123

## Funcionalidades por Tipo de Usuário

### RH (Recursos Humanos)
- ✅ Adicionar novas vagas
- ✅ Editar vagas existentes
- ✅ Excluir vagas
- ✅ Visualizar estatísticas de vagas criadas
- ✅ Gerenciar candidatos

### Candidatos
- ✅ Visualizar vagas disponíveis
- ✅ Filtrar vagas por título e localização
- ✅ Ver detalhes completos das vagas
- ✅ Acessar página de conta com informações pessoais

## Melhorias Implementadas

1. **Interface Responsiva:** Design adaptável para desktop e mobile
2. **Sistema de Filtros:** Busca por título e localização
3. **Modal para Vagas:** Interface intuitiva para adicionar vagas
4. **Estatísticas em Tempo Real:** Dados atualizados automaticamente
5. **Histórico de Atividades:** Registro das ações recentes do usuário
6. **Validação de Formulários:** Campos obrigatórios e validações
7. **Proteção CSRF:** Configurada para acesso externo seguro

## Tecnologias Utilizadas

- **Backend:** Django 5.2.4
- **Frontend:** HTML5, CSS3, JavaScript
- **Banco de Dados:** SQLite (padrão do Django)
- **Autenticação:** Sistema nativo do Django
- **Responsividade:** CSS Grid e Flexbox

## Status do Projeto

✅ **Concluído** - Todas as funcionalidades solicitadas foram implementadas e testadas com sucesso.

## Próximos Passos (Sugestões)

- [ ] Sistema de candidaturas para vagas
- [ ] Notificações por email
- [ ] Upload de currículos
- [ ] Sistema de avaliação de candidatos
- [ ] Dashboard analítico avançado
- [ ] API REST para integração externa

