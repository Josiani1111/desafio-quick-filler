# 📄 Quick Filler

Aplicação web desenvolvida com **Python e FastAPI** para recebimento, processamento e extração de informações de documentos PDF, incluindo **holerites (Payroll)** e **cartões de ponto**.

O projeto foi desenvolvido como um **desafio técnico**, com foco em desenvolvimento de APIs, processamento de documentos, parsing, expressões regulares, OCR e geração de dados estruturados em planilhas Excel.

---

## 🌐 Aplicação online

A aplicação está disponível publicamente:

**https://quick-filler-josiani.onrender.com**

---

## 🎯 Objetivo

O Quick Filler foi desenvolvido para automatizar o processamento de documentos PDF e transformar informações não estruturadas em dados organizados.

A aplicação é capaz de:

* 📄 Receber documentos PDF;
* 🔎 Identificar o tipo de documento;
* ⚙️ Processar diferentes formatos;
* 🧩 Extrair informações utilizando regras específicas;
* 🔤 Utilizar expressões regulares para identificar dados;
* 🖨️ Utilizar OCR quando necessário;
* 📊 Gerar dados estruturados em planilhas Excel;
* 🗂️ Registrar documentos processados.

---

## 🚀 Funcionalidades

* Upload de arquivos PDF;
* Processamento de cartões de ponto;
* Processamento de holerites (Payroll);
* Extração de texto de documentos PDF;
* Parsing utilizando expressões regulares;
* Identificação de dias e horários;
* Classificação de horários como `IN` e `OUT`;
* Processamento de diferentes formatos de Payroll;
* OCR para documentos que necessitam de reconhecimento de texto;
* Registro de documentos processados;
* Consulta do histórico;
* Geração de planilhas Excel.

---

## 🏗️ Arquitetura da solução

A aplicação utiliza **FastAPI** como estrutura principal da API.

O endpoint `/upload` recebe o documento PDF e direciona o processamento para o parser correspondente.

### 🕒 Cartões de ponto

Para cartões de ponto, o sistema:

1. Lê o conteúdo do PDF;
2. Identifica os dias;
3. Identifica os horários registrados;
4. Classifica os horários alternadamente como `IN` e `OUT`;
5. Organiza os resultados;
6. Aplica regras para evitar duplicação de informações;
7. Ignora informações de rodapé que não fazem parte dos registros.

O processamento está implementado em `parser.py`.

### 💰 Holerites / Payroll

Para documentos de Payroll, foram desenvolvidas regras específicas para diferentes formatos.

O sistema realiza a extração de informações como:

* Mês;
* Período;
* Salário líquido;
* Valores relacionados aos proventos.

Foram tratados os documentos:

* Payroll 01
* Payroll 02
* Payroll 03
* Payroll 04

O processamento está implementado em `parser_payroll.py`.

---

## 🔤 OCR

Quando o PDF não apresenta texto suficiente para a extração convencional, a aplicação utiliza **OCR (Optical Character Recognition)**.

O fluxo de processamento utiliza:

1. **PyMuPDF** para abrir o PDF;
2. Renderização da página como imagem;
3. **PyTesseract** para reconhecimento do texto;
4. Utilização do idioma português (`por`);
5. Envio do texto extraído para o parser de Payroll.

O processamento está implementado em `ocr_payroll.py`.

---

## 🔗 API

| Método | Endpoint     | Descrição                          |
| ------ | ------------ | ---------------------------------- |
| `GET`  | `/`          | Verifica se a API está funcionando |
| `GET`  | `/healthz`   | Endpoint de verificação de saúde   |
| `GET`  | `/app`       | Disponibiliza a interface web      |
| `GET`  | `/historico` | Consulta documentos processados    |
| `POST` | `/upload`    | Recebe e processa documentos PDF   |

---

## 📊 Resultados

Foram geradas planilhas Excel a partir dos documentos de exemplo.

### Payroll

* `payroll-01.xlsx`
* `payroll-02.xlsx`
* `payroll-03.xlsx`
* `payroll-04.xlsx`

### Cartões de ponto

* `time-card-01.xlsx`
* `time-card-02.xlsx`
* `time-card-03.xlsx`
* `time-card-04.xlsx`

---

## 🛠️ Tecnologias utilizadas

### Backend

* 🐍 Python
* ⚡ FastAPI
* 🚀 Uvicorn

### Processamento de documentos

* 📄 pypdf
* 📑 PyMuPDF
* 🔤 PyTesseract
* 🖼️ Pillow
* 🔎 Expressões regulares

### Dados e arquivos

* 🗄️ SQLite
* 📊 OpenPyXL

### Frontend e ferramentas

* 🌐 HTML5
* ⚡ JavaScript
* 🔧 Git
* 🐙 GitHub
* ☁️ Render

---

## 📁 Estrutura do projeto

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

---

## ▶️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Josiani1111/desafio-quick-filler.git
```

### 2. Acesse a pasta

```bash
cd desafio-quick-filler
```

### 3. Crie o ambiente virtual

```powershell
py -m venv .venv
```

### 4. Ative o ambiente virtual

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 6. Execute a aplicação

```powershell
uvicorn app.main:app --reload
```

### 7. Acesse no navegador

```text
http://127.0.0.1:8000
```

---

## 📚 Conhecimentos praticados

Durante o desenvolvimento deste projeto, foram aplicados conhecimentos de:

* Desenvolvimento de APIs com **FastAPI**;
* Desenvolvimento web com Python;
* Upload e processamento de arquivos;
* Manipulação de documentos PDF;
* Criação de parsers;
* Expressões regulares;
* Processamento de diferentes formatos de documentos;
* OCR;
* Manipulação de imagens;
* Banco de dados SQLite;
* Geração de planilhas Excel;
* Integração entre backend e interface web;
* Testes locais;
* Git e GitHub;
* Publicação de aplicações web.

---

## 🎯 Objetivo profissional

Este projeto faz parte da minha formação em **Análise e Desenvolvimento de Sistemas** e da construção do meu portfólio na área de Tecnologia.

O desenvolvimento do Quick Filler permitiu aplicar conhecimentos de **Python, APIs, processamento de documentos, OCR, bancos de dados e automação**, transformando um desafio técnico em uma aplicação prática.

---

## 👩‍💻 Desenvolvedora

**Josiani Oliveira**

Estudante do último ano de **Análise e Desenvolvimento de Sistemas**.

Busco uma oportunidade como **Desenvolvedora Júnior**, especialmente em posições relacionadas a **Python, backend, APIs REST, automação e desenvolvimento de sistemas**.

---

⭐ Obrigada por visitar este projeto!
