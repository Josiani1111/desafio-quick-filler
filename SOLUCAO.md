\# SOLUÇÃO — Quick Filler



\## Objetivo



Desenvolver uma aplicação web capaz de receber documentos PDF contendo cartões de ponto e holerites, extrair as informações relevantes e disponibilizar os dados processados.



\## Tecnologias utilizadas



\- Python

\- FastAPI

\- Uvicorn

\- pypdf

\- PyMuPDF

\- PyTesseract

\- Pillow

\- OpenPyXL

\- HTML

\- JavaScript

\- Git e GitHub



\## Arquitetura da solução



A aplicação foi desenvolvida utilizando FastAPI.



O endpoint `/upload` recebe o arquivo PDF enviado pelo usuário.



A aplicação identifica o tipo de documento pelo nome do arquivo e direciona o processamento para o parser correspondente.



\### Cartões de ponto



Para cartões de ponto, o sistema:



1\. Lê o conteúdo do PDF.

2\. Identifica os dias.

3\. Identifica os horários registrados.

4\. Classifica os horários alternadamente como `IN` e `OUT`.

5\. Organiza os resultados por página.



O processamento está implementado em `parser.py`.



\### Holerites / Payroll



Para os documentos de payroll, o sistema utiliza diferentes regras de extração conforme o formato do documento.



O processamento está implementado em `parser\_payroll.py`.



Foram tratados os documentos Payroll 01, Payroll 02, Payroll 03 e Payroll 04.



\### OCR



Quando o PDF não possui texto suficiente para a extração convencional, a aplicação utiliza OCR.



O fluxo de OCR é:



1\. Abrir o PDF com PyMuPDF.

2\. Renderizar a página como imagem.

3\. Processar a imagem utilizando PyTesseract.

4\. Utilizar o idioma português (`por`).

5\. Enviar o texto obtido para o parser de payroll.



O código de OCR está em `ocr\_payroll.py`.



\## API



\### GET `/`



Retorna uma mensagem indicando que a API está funcionando.



\### GET `/healthz`



Endpoint utilizado para verificar a saúde da aplicação.



\### GET `/app`



Disponibiliza a interface web da aplicação.



\### POST `/upload`



Recebe o PDF enviado pelo usuário e realiza o processamento do documento.



\## Resultados



Foram geradas planilhas para os documentos de exemplo:



\- payroll-01.xlsx

\- payroll-02.xlsx

\- payroll-03.xlsx

\- payroll-04.xlsx

\- time-card-01.xlsx

\- time-card-02.xlsx

\- time-card-03.xlsx

\- time-card-04.xlsx



\## Conclusão



A solução demonstra o uso de Python e FastAPI para criação de uma aplicação web, processamento de documentos PDF, utilização de expressões regulares, OCR e geração de dados estruturados.

