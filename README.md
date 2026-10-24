# Sistema Pizzaria

Sistema de gerenciamento de pizzaria desenvolvido com Django como projeto final de curso de Python. O objetivo do projeto foi criar uma aplicação completa de CRUD, com autenticação de usuários, banco de dados, templates responsivos e interface amigável para controle de produtos.

## Visão geral

Este projeto simula o painel administrativo de uma pizzaria, permitindo que o usuário:

- crie uma conta e faça login;
- cadastre novas pizzas;
- visualize todas as pizzas em uma listagem;
- edite os dados de uma pizza existente;
- exclua registros;
- busque pizzas por nome;
- mantenha os dados organizados por categoria.

A aplicação foi pensada como um projeto prático para consolidar conceitos de Python, Django, autenticação, models, formulários, rotas, templates e integração com banco de dados.

## Funcionalidades principais

### 1. Autenticação de usuários

A aplicação conta com um sistema de login e cadastro de usuário usando o mecanismo nativo do Django.

- cadastro de novos usuários;
- login com username e senha;
- validação de senha e confirmação;
- prevenção de usuários duplicados;
- bloqueio de acesso a páginas internas sem autenticação.

As views de autenticação estão na app `apps/login` e utilizam `authenticate`, `login`, `logout` e o model `User` do Django.

### 2. CRUD completo de pizzas

A funcionalidade principal do sistema está na app `apps/crud`, onde o usuário pode realizar operações completas sobre uma entidade `Pizza`.

- criar nova pizza;
- listar pizzas cadastradas;
- alterar dados da pizza;
- excluir pizza;
- buscar pizza por nome.

A model `Pizza` possui os campos:

- `nome`
- `preco`
- `categoria`
- `ingredientes`

### 3. Organização por categorias

As pizzas podem ser classificadas em categorias, como:

- Tradicional
- Especial
- Doce

Essa estrutura foi implementada com `choices` no campo `categoria`, deixando a organização mais clara e facilitando futuras expansões.

### 4. Busca e filtragem

A aplicação possui uma funcionalidade de busca por nome da pizza, com filtro case-insensitive (`icontains`). Isso ajuda a localizar rapidamente uma pizza específica na base de dados.

### 5. Validação e tratamento de dados

O projeto usa `ModelForm` e campos personalizados para garantir que os dados sejam validados corretamente.

Exemplos:

- preço com conversão de moeda no formato `R$ 39,90`;
- validação de valor mínimo;
- controle de campos obrigatórios;
- mensagens de erro exibidas no formulário.

### 6. Interface visual moderna

A parte visual foi construída com templates HTML e estilização por meio de:

- Tailwind CSS;
- DaisyUI;
- Font Awesome;
- JavaScript para pequenas interações front-end.

A interface foi pensada para apresentar um visual mais profissional, com layout em tons escuros e elementos card-style, com foco em usabilidade e boa experiência visual.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Tailwind CSS
- DaisyUI
- JavaScript
- Git/GitHub

## Estrutura do projeto

```text
Sistema-Pizzaria/
├── apps/
│   ├── crud/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   └── login/
│       ├── templates/
│       ├── urls.py
│       ├── views.py
│       └── ...
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.pizzaria.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── ...
```

## Como foi construído

O projeto foi criado seguindo a arquitetura padrão do Django:

1. Criação do projeto principal em `config/` com `django-admin startproject`.
2. Separação das funcionalidades em apps:
   - `apps/login` para autenticação;
   - `apps/crud` para gerenciamento das pizzas.
3. Definição da model `Pizza` em `apps/crud/models.py`.
4. Criação dos formulários em `apps/crud/forms.py` para validar os dados da pizza.
5. Desenvolvimento das views em `apps/crud/views.py` para renderizar e processar os formulários.
6. Configuração das rotas em `apps/crud/urls.py` e `apps/login/urls.py`.
7. Implementação dos templates na pasta `templates` para o frontend do sistema.
8. Configuração do banco de dados SQLite no `settings.py`.
9. Uso de autenticação do Django para proteger páginas internas com `@login_required`.

## Banco de dados

O projeto utiliza SQLite como banco de dados local, que é simples, leve e ideal para aplicações de estudo e pequenos projetos.

O banco armazena as pizzas cadastradas e mantém a estrutura definida pelo modelo do Django. Isso permite persistência dos dados sem necessidade de configuração extra de banco em ambiente local.

## CSS e frontend

A parte visual foi um ponto importante do projeto. O frontend foi trabalhado com:

- HTML estruturado;
- templates reutilizáveis;
- classes utilitárias do Tailwind;
- uso do DaisyUI para melhorar a aparência dos componentes;
- estilos para formulários, botões, cards e páginas de login.

Além disso, o projeto usa arquivos estáticos em `apps/crud/static/js` e configurações do Django para servir recursos HTML/CSS/JS de forma organizada.

## P.Q. do projeto

O objetivo didático do projeto foi consolidar os conceitos aprendidos no curso de Python, principalmente em relação ao framework Django.

O "P.Q." (projeto-qualificação / propósito do projeto) foi criar uma aplicação funcional e completa, que reunisse os principais pilares do desenvolvimento web:

- autenticação;
- CRUD;
- organização em apps;
- modelagem de dados;
- templates;
- uso de banco de dados;
- frontend com CSS moderno;
- boas práticas de estrutura MVC/MVT.

Em outras palavras, esse projeto representa a etapa final em que o aluno coloca em prática, de forma integrada, vários conhecimentos adquiridos durante o curso.

## Como rodar o projeto

### 1. Crie um ambiente virtual

```bash
python -m venv venv
```

### 2. Ative o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

Acesse:

```text
http://localhost:8000/
```

## Observações

- O projeto foi desenvolvido como exemplo de aplicação web completa em Django.
- O foco principal está no aprendizado prático e na aplicação dos conceitos do curso.
- O sistema pode ser expandido futuramente para incluir pedidos, clientes, carrinho, relatórios e painel administrativo mais completo.

## Contribuição

Este projeto foi elaborado como exercício acadêmico e de aprendizagem. Qualquer melhoria, refatoração ou expansão é bem-vinda.

## Autor

Projeto desenvolvido como parte de um curso de Python/Django, com foco em criação de um sistema completo de gestão de pizzaria.

---

Se quiser, também posso preparar uma segunda versão do README com um visual mais profissional de portfolio, com badges, screenshots e uma apresentação mais "GitHub-ready".
