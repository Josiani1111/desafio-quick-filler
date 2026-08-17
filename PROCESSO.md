\# PROCESSO — Quick Filler



\## 1. Preparação do ambiente



O projeto foi desenvolvido em Python utilizando um ambiente virtual (`.venv`).



Foram utilizadas bibliotecas para criação da API, processamento de PDF, OCR e geração das planilhas.



\## 2. Desenvolvimento da API



Foi criada uma aplicação utilizando FastAPI.



Foram implementados endpoints para:



\- verificar o funcionamento da API;

\- verificar a saúde da aplicação;

\- disponibilizar a interface web;

\- receber arquivos PDF.



\## 3. Processamento dos documentos



Inicialmente foi utilizada a extração de texto dos PDFs.



Para documentos com texto disponível, foi utilizado `pypdf`.



A partir do texto extraído foram criados parsers utilizando expressões regulares.



\## 4. Parser de cartões de ponto



Foi desenvolvido um parser para identificar:



\- dia;

\- dia da semana;

\- horários registrados;

\- entrada (`IN`);

\- saída (`OUT`).



Também foram adicionadas regras para evitar duplicação de dias e ignorar informações de rodapé.



\## 5. Parser de Payroll



Foram analisados os diferentes formatos dos documentos de exemplo.



Foram criadas regras específicas para localizar:



\- mês;

\- período;

\- salário líquido;

\- valores relacionados aos proventos.



O parser foi adaptado para os diferentes formatos dos documentos Payroll 01 a 04.



\## 6. OCR



Para documentos que não apresentavam texto suficiente na extração convencional, foi implementado um fluxo utilizando OCR.



O PDF é convertido em imagem e processado pelo Tesseract através do PyTesseract.



O idioma utilizado no processamento OCR é o português.



\## 7. Geração das planilhas



Após o processamento dos documentos, foram geradas planilhas Excel utilizando OpenPyXL.



Foram produzidos resultados para os documentos de exemplo de payroll e cartões de ponto.



\## 8. Testes



Durante o desenvolvimento foram realizados testes locais da API e do upload dos documentos.



A aplicação foi executada utilizando Uvicorn.



Também foram utilizados documentos de exemplo para verificar a extração dos dados.



\## 9. Controle de versão



O projeto foi organizado utilizando Git e disponibilizado em um repositório público no GitHub.



\## 10. Resultado final



Ao final do desenvolvimento, a aplicação permite enviar documentos PDF, processar os dados e retornar as informações estruturadas.



Também foram geradas as planilhas correspondentes aos documentos de exemplo.

