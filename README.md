# Django FBV to CBV Refactoring

CRUD de Contatos desenvolvido em Django demonstrando a refatoração de Function-Based Views (FBV) para Class-Based Views (CBV).

## Objetivo

Demonstrar na prática as diferenças entre os dois estilos de views do Django, com histórico de commits que documenta cada etapa da refatoração.

## Tecnologias

- Python 3.13
- Django 6.0

## Funcionalidades

- Listar contatos
- Cadastrar contato
- Editar contato
- Detalhar contato
- Deletar contato

## Como executar

```bash
git clone https://github.com/silviolpiresdev/django-fbv-to-cbv-refactoring.git
cd django-fbv-to-cbv-refactoring
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/contatos/`

## Estrutura dos commits

- `feat`: CRUD completo em FBV
- `chore`: configuração do .gitignore
- `refactor`: migração para CBV