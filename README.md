 📄 Quick Filler

Aplicação web desenvolvida em **Python e FastAPI** para recebimento, processamento e extração de informações de documentos PDF, incluindo **holerites (Payroll)** e **cartões de ponto**.

O projeto foi desenvolvido como desafio técnico, com foco em **desenvolvimento de APIs, processamento de documentos, expressões regulares, OCR e geração de dados estruturados em planilhas Excel**.

 🌐 Aplicação pública

A aplicação está disponível online:

https://quick-filler-josiani.onrender.com

🎯 Objetivo

Desenvolver uma aplicação capaz de:

* receber documentos PDF;
* identificar o tipo de documento;
* extrair informações relevantes;
* processar os dados utilizando regras específicas;
* utilizar OCR quando a extração convencional não for suficiente;
* retornar os dados processados;
* gerar planilhas Excel a partir dos documentos de exemplo.

🚀 Funcionalidades

* Upload de arquivos PDF;
* Processamento de cartões de ponto;
* Processamento de holerites (Payroll);
* Extração de texto de PDFs;
* Extração de informações utilizando expressões regulares;
* Identificação de dias e horários;
* Classificação de horários como `IN` e `OUT`;
* Processamento de diferentes formatos de Payroll;
* OCR para documentos que necessitam de reconhecimento de texto;
* Registro dos documentos processados;
* Consulta do histórico de documentos;
* Geração de planilhas Excel.

 🏗️ Arquitetura da solução

A aplicação utiliza **FastAPI** como estrutura principal da API.

O endpoint `/upload` recebe o arquivo PDF e identifica o tipo de documento pelo nome do arquivo, direcionando o processamento para o parser correspondente.

 Cartões de ponto

Para cartões de ponto, o sistema:

1. Lê o conteúdo do PDF;
2. Identifica os dias;
3. Identifica os horários registrados;
4. Classifica os horários alternadamente como `IN` e `OUT`;
5. Organiza os resultados por página;
6. Aplica regras para evitar duplicação de dias e ignorar informações de rodapé.

O processamento está implementado em `parser.py`.

 Holerites / Payroll

Para documentos de Payroll, foram desenvolvidas regras específicas para diferentes formatos.

O sistema realiza a extração de informações como:

* mês;
* período;
* salário líquido;
* valores relacionados aos proventos.

Foram tratados os documentos **Payroll 01, 02, 03 e 04**.

O processamento está implementado em `parser_payroll.py`.

 OCR

Quando o PDF não apresenta texto suficiente para a extração convencional, a aplicação utiliza OCR.

O fluxo é:

1. Abrir o PDF utilizando **PyMuPDF**;
2. Renderizar a página como imagem;
3. Processar a imagem utilizando **PyTesseract**;
4. Utilizar o idioma português (`por`);
5. Enviar o texto obtido para o parser de Payroll.

O código está implementado em `ocr_payroll.py`.

 🔗 API

`GET /`

Retorna uma mensagem indicando que a API está funcionando.

 `GET /healthz`

Endpoint utilizado para verificar a saúde da aplicação.

 `GET /app`

Disponibiliza a interface web da aplicação.

 `GET /historico`

Retorna os documentos processados registrados no banco de dados.

 `POST /upload`

Recebe o arquivo PDF enviado pelo usuário e realiza o processamento do documento.

 📊 Resultados

Foram geradas planilhas Excel para os documentos de exemplo:

 Payroll

* `payroll-01.xlsx`
* `payroll-02.xlsx`
* `payroll-03.xlsx`
* `payroll-04.xlsx`

 Cartões de ponto

* `time-card-01.xlsx`
* `time-card-02.xlsx`
* `time-card-03.xlsx`
* `time-card-04.xlsx`

 🛠️ Tecnologias utilizadas

* **Python**
* **FastAPI**
* **Uvicorn**
* **pypdf**
* **PyMuPDF**
* **PyTesseract**
* **Pillow**
* **OpenPyXL**
* **HTML5**
* **JavaScript**
* **Git**
* **GitHub**
* **Render**

 📁 Estrutura do projeto

```text
desafio-quick-filler/
│
├── app/
│   ├── __init__.py
│   ├── index.html
│   ├── main.py
│   ├── parser.py
│   ├── parser_payroll.py
│   ├── ocr_payroll.py
│   └── database.py
│
├── pdfs/
├── planilhas/
├── PROCESSO.md
├── README.md
├── SOLUCAO.md
├── requirements.txt
└── .gitignore
```

 ▶️ Como executar localmente

 1. Clone o repositório

Clone o projeto para o seu computador.

 2. Acesse a pasta

Abra o **PowerShell** dentro da pasta do projeto.

 3. Crie o ambiente virtual

```powershell
py -m venv .venv
```

 4. Ative o ambiente virtual

```powershell
.venv\Scripts\Activate.ps1
```

 5. Instale as dependências

```powershell
pip install -r requirements.txt
```

  6. Execute a aplicação

```powershell
uvicorn app.main:app --reload
```

7. Acesse no navegador

```text
http://127.0.0.1:8000
```

 📚 Conhecimentos praticados

Durante o desenvolvimento deste projeto, foram praticados:

* Desenvolvimento de APIs com **FastAPI**;
* Desenvolvimento web com Python;
* Upload e processamento de arquivos;
* Manipulação de documentos PDF;
* Expressões regulares;
* Criação de parsers;
* Processamento de documentos com diferentes formatos;
* OCR;
* Manipulação de imagens;
* Banco de dados SQLite;
* Geração de planilhas Excel;
* Integração entre backend e interface web;
* Testes locais;
* Git e GitHub;
* Publicação de aplicação web.

## 🎯 Objetivo profissional

Este projeto faz parte da minha formação em **Análise e Desenvolvimento de Sistemas** e da construção do meu portfólio na área de tecnologia.

O desenvolvimento do Quick Filler permitiu aplicar conhecimentos de **Python, APIs, processamento de documentos, OCR, bancos de dados e automação**, transformando um desafio técnico em uma aplicação prática.

## 👩‍💻 Desenvolvedora

**Josiani Oliveira**

Estudante do último ano de Análise e Desenvolvimento de Sistemas.

---

⭐ Obrigada por visitar este projeto!

 
