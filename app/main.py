from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pypdf import PdfReader
import os
from pathlib import Path

from app.parser import extrair_cartao_ponto


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent


@app.get("/")
def inicio():
    return {
        "mensagem": "API do Desafio Quick Filler funcionando!"
    }


@app.get("/healthz")
def healthz():
    return {
        "status": "ok"
    }


@app.get("/app")
def pagina():
    return FileResponse(BASE_DIR / "index.html")


@app.post("/upload")
async def upload_pdf(arquivo: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    caminho = os.path.join("uploads", arquivo.filename)

    with open(caminho, "wb") as arquivo_salvo:
        conteudo = await arquivo.read()
        arquivo_salvo.write(conteudo)

    print("UPLOAD RECEBIDO:", arquivo.filename)

    leitor = PdfReader(caminho)

    resultado = []

    for numero_pagina, pagina_pdf in enumerate(leitor.pages, start=1):

        texto = pagina_pdf.extract_text() or ""

        print("========== PÁGINA", numero_pagina, "==========")
        print(texto)
        print("==============================================")

        dados = extrair_cartao_ponto(
            texto,
            numero_pagina
        )

        resultado.append(dados)

    return {
        "mensagem": "PDF processado com sucesso!",
        "arquivo": arquivo.filename,
        "paginas": resultado
    }