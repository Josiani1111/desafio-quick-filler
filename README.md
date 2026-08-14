# Quick Filler

Sistema desenvolvido em **Python e FastAPI** para upload, leitura e processamento de arquivos PDF contendo informações de cartões de ponto.

O projeto foi desenvolvido como **desafio técnico**, com foco em desenvolvimento de API, processamento de documentos PDF e apresentação dos dados em uma interface web.

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* pypdf
* PyMuPDF
* OpenPyXL
* HTML
* JavaScript
* Git
* GitHub

## Funcionalidades

* Upload de arquivos PDF;
* Leitura das páginas do PDF;
* Extração de informações dos cartões de ponto;
* Identificação dos dias;
* Identificação dos horários registrados;
* Processamento dos dados;
* Exibição dos resultados no navegador.

## Estrutura do projeto

```text
desafio-quick-filler/
├── app/
│   ├── __init__.py
│   ├── index.html
│   ├── main.py
│   ├── parser.py
│   └── teste_pdf.py
├── pdfs/
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar o projeto

### 1. Criar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

### 2. Ativar o ambiente virtual

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 4. Iniciar a aplicação

```powershell
uvicorn app.main:app --host 127.0.0.1 --port 8001
```

### 5. Acessar no navegador

```text
http://127.0.0.1:8001/app
```

## Exemplo de uso

O usuário seleciona um arquivo PDF de cartão de ponto e envia o documento pelo formulário.

A aplicação processa o arquivo e apresenta os dias e horários identificados no navegador.

## Objetivo

Demonstrar conhecimentos práticos em:

* Desenvolvimento de APIs com FastAPI;
* Programação em Python;
* Processamento de arquivos PDF;
* Manipulação e extração de dados;
* Desenvolvimento de interface web;
* Organização de projetos;
* Controle de versão com Git e GitHub.

## Autora

**Josiani C. de Oliveira**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento de software e aprimoramento de conhecimentos em Python, APIs, SQL e testes de software.















































































































































