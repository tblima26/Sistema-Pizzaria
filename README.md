
# 🍕 Sistema Pizzaria

<p align="center">
  Sistema de gerenciamento de pizzaria desenvolvido com Django como projeto final de um curso de Python.
  <br>
  Uma aplicação web para praticar autenticação, CRUD, persistência de dados e desenvolvimento de interfaces.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

---

## 📌 Sobre o projeto

O **Sistema Pizzaria** é uma aplicação web desenvolvida para consolidar os conhecimentos adquiridos durante um curso de Python, utilizando o framework Django.

O sistema oferece um painel administrativo para gerenciar pizzas, com autenticação de usuários, cadastro de produtos, edição, exclusão, pesquisa e organização por categorias.

O projeto reúne conceitos fundamentais do desenvolvimento web, desde a modelagem dos dados até a construção de uma interface responsiva.

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|:--|:--|
| 🔐 Autenticação | Cadastro, login e logout de usuários. |
| ➕ Cadastro | Inclusão de novas pizzas no sistema. |
| 📋 Listagem | Visualização das pizzas cadastradas. |
| ✏️ Edição | Atualização dos dados de uma pizza. |
| 🗑️ Exclusão | Remoção de pizzas cadastradas. |
| 🔎 Pesquisa | Busca por nome, sem distinção entre maiúsculas e minúsculas. |
| 🏷️ Categorias | Organização das pizzas por tipo. |
| ✅ Validação | Verificação dos dados enviados pelos formulários. |
| 💬 Mensagens | Exibição de erros e validações nos formulários. |
| 🔒 Proteção | Restrição de acesso às páginas internas para usuários não autenticados. |

## 🍕 Gerenciamento de pizzas

Cada pizza possui os seguintes campos:

| Campo | Descrição |
|:--|:--|
| `nome` | Nome da pizza. |
| `preco` | Preço da pizza, com tratamento de valores monetários. |
| `categoria` | Categoria selecionada entre as opções disponíveis. |
| `ingredientes` | Ingredientes utilizados na pizza. |

### Categorias disponíveis

- **Tradicional**
- **Especial**
- **Doce**

As categorias são definidas utilizando `choices` no modelo Django, facilitando a padronização dos registros.

## 🔑 Autenticação de usuários

O sistema utiliza o mecanismo nativo de autenticação do Django, com as operações de cadastro, login e logout.

Entre os recursos implementados estão:

- Cadastro de usuários.
- Autenticação com nome de usuário e senha.
- Confirmação e validação de senha.
- Prevenção de nomes de usuário duplicados.
- Proteção de páginas internas por meio de `@login_required`.

As funcionalidades de autenticação estão organizadas na aplicação `apps/login`.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|:--|:--|
| [Python](https://www.python.org/) | Linguagem de programação. |
| [Django](https://www.djangoproject.com/) | Framework web e gerenciamento da aplicação. |
| [SQLite](https://www.sqlite.org/) | Banco de dados relacional local. |
| [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML) | Estrutura das páginas. |
| [Tailwind CSS](https://tailwindcss.com/) | Estilização por classes utilitárias. |
| [DaisyUI](https://daisyui.com/) | Componentes visuais para a interface. |
| [Font Awesome](https://fontawesome.com/) | Ícones da interface. |
| [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) | Interações no frontend. |
| [Git](https://git-scm.com/) | Controle de versão. |
| [GitHub](https://github.com/) | Hospedagem do código-fonte. |

## 🏗️ Arquitetura do projeto

A aplicação segue a organização MVT do Django, separando modelos, views e templates, com funcionalidades divididas em aplicações específicas.

```text
Sistema-Pizzaria/
│
├── apps/
│   ├── crud/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   │
│   └── login/
│       ├── templates/
│       ├── urls.py
│       ├── views.py
│       └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.pizzaria.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

### Organização das aplicações

- **`apps/crud`**: gerenciamento das pizzas, modelos, formulários, views e templates relacionados.
- **`apps/login`**: autenticação e gerenciamento do acesso dos usuários.
- **`config`**: configurações gerais, rotas principais e arquivos de inicialização do projeto.
- **`manage.py`**: utilitário de linha de comando do Django.
- **`requirements.txt`**: dependências necessárias para executar a aplicação.

## 🗄️ Banco de dados

O projeto utiliza SQLite, um banco de dados relacional leve, adequado para desenvolvimento local e projetos de aprendizado.

Os modelos Django definem a estrutura dos dados, enquanto as migrações permitem criar e atualizar as tabelas do banco.

O arquivo de banco de dados incluído na estrutura é `db.pizzaria.sqlite3`.

## 🎨 Interface e experiência visual

A interface utiliza uma combinação de tecnologias para proporcionar uma experiência organizada e agradável.

- **Tailwind CSS:** estilização responsiva e consistente.
- **DaisyUI:** componentes visuais e elementos de interface.
- **Font Awesome:** ícones para melhorar a identificação das ações.
- **JavaScript:** pequenas interações no frontend.
- **Templates Django:** reutilização da estrutura HTML entre as páginas.

O visual utiliza tons escuros e componentes em formato de cards, priorizando a organização das informações e a facilidade de navegação.

## ⚙️ Como executar o projeto

### Pré-requisitos

- Python instalado.
- Git instalado, caso deseje clonar o repositório.
- Terminal ou editor de código de sua preferência.

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd Sistema-Pizzaria
```

> Substitua `URL_DO_REPOSITORIO` pelo endereço real do repositório.

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

### 7. Acesse a aplicação

Abra o navegador no endereço:

**http://localhost:8000/**

## 🎯 Objetivos de aprendizagem

Este projeto foi desenvolvido com o propósito de aplicar, de maneira integrada, os principais conceitos estudados durante a formação em Python e Django.

Os conhecimentos praticados incluem:

- Desenvolvimento de aplicações web com Django.
- Organização de funcionalidades em apps.
- Criação e manipulação de modelos.
- Operações CRUD completas.
- Autenticação e controle de acesso.
- Construção e validação de formulários.
- Consultas e filtros no banco de dados.
- Uso de templates e arquivos estáticos.
- Desenvolvimento de interfaces com Tailwind CSS.
- Controle de versão com Git.

## 🚀 Possíveis melhorias futuras

O projeto pode ser expandido para contemplar novas funcionalidades, como:

- Cadastro e gerenciamento de clientes.
- Registro e acompanhamento de pedidos.
- Carrinho de compras.
- Relatórios de vendas.
- Painel administrativo ampliado.

Essas melhorias são possibilidades futuras e não fazem parte das funcionalidades descritas na versão atual.

## 🤝 Contribuição

Este projeto foi desenvolvido como exercício acadêmico e de aprendizagem. Sugestões, melhorias e refatorações são bem-vindas.

## 👨‍💻 Autor

Projeto desenvolvido como parte de um curso de Python e Django, com foco na construção de uma aplicação web completa para gerenciamento de pizzaria.

---

<p align="center">
  Desenvolvido para praticar, aprender e evoluir na programação. 🍕
</p>
