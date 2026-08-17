import fitz
import pytesseract
from PIL import Image
import io


def extrair_ocr_pdf(caminho_pdf):

    documento = fitz.open(caminho_pdf)

    resultados = []

    for numero_pagina, pagina in enumerate(documento, start=1):

        pix = pagina.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )

        imagem = Image.open(
            io.BytesIO(pix.tobytes("png"))
        )

        texto = pytesseract.image_to_string(
            imagem,
            lang="por"
        )

        resultados.append({
            "pagina": numero_pagina,
            "texto": texto
        })

    documento.close()

    return resultados