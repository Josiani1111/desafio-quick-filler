from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pypdf import PdfReader
import os
from pathlib import Path

from app.parser import extrair_cartao_ponto
from app.parser_payroll import extrair_payroll
from app.ocr_payroll import extrair_ocr_pdf


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

    # ========================================================
    # PAYROLL
    # ========================================================

    if arquivo.filename.lower().startswith("payroll"):

        leitor = PdfReader(caminho)

        resultado = []

        for numero_pagina, pagina_pdf in enumerate(
            leitor.pages,
            start=1
        ):

            texto = pagina_pdf.extract_text() or ""

            # Se o PDF não possui texto suficiente,
            # usamos OCR.
            if len(texto.strip()) < 100:

                dados_ocr = extrair_ocr_pdf(caminho)

                texto = dados_ocr[
                    numero_pagina - 1
                ]["texto"]

            dados = extrair_payroll(
                texto,
                numero_pagina
            )

            resultado.extend(dados)

        return {
            "mensagem": "Payroll processado com sucesso!",
            "arquivo": arquivo.filename,
            "paginas": resultado
        }


    # ========================================================
    # CARTÃO DE PONTO
    # ========================================================

    leitor = PdfReader(caminho)

    resultado = []

    for numero_pagina, pagina_pdf in enumerate(
        leitor.pages,
        start=1
    ):

        texto = pagina_pdf.extract_text() or ""

        print(
            "========== PÁGINA",
            numero_pagina,
            "=========="
        )

        print(texto)

        print(
            "=============================================="
        )

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