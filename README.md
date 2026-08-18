# Quick Filler

Sistema desenvolvido em Python e FastAPI para upload, leitura e processamento de arquivos PDF contendo informações de holerites e cartões de ponto.

Projeto desenvolvido como desafio técnico, com foco em desenvolvimento de API, processamento de documentos PDF, extração de dados e apresentação dos resultados em uma interface web.

## Aplicação pública

A aplicação está disponível para acesso online:

https://quick-filler-josiani.onrender.com

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- pypdf
- PyMuPDF
- PyTesseract
- OpenPyXL
- HTML
- JavaScript
- Git
- GitHub
- Render

## Funcionalidades

- Upload de arquivos PDF;
- Leitura das páginas dos documentos;
- Extração de informações de holerites;
- Extração de informações de cartões de ponto;
- Identificação dos dias;
- Identificação dos horários registrados;
- Processamento dos dados extraídos;
- Apresentação dos resultados no navegador;
- Geração de planilhas Excel a partir dos documentos processados.

### Estrutura do projeto

desafio-quick-filler/
├── app/
│   ├── __init__.py
│   ├── index.html
│   ├── main.py
│   ├── parser.py
│   ├── ocr_payroll.py
│   └── teste_pdf.py
├── pdfs/
├── planilhas/
├── PROCESSO.md
├── README.md
├── SOLUCAO.md
├── requirements.txt
└── .gitignore