from pathlib import Path

from openpyxl import Workbook
from pypdf import PdfReader

from parser import extrair_cartao_ponto


PDF = Path("pdfs/time-card-01.pdf")
PASTA_SAIDA = Path("planilhas")
ARQUIVO_SAIDA = PASTA_SAIDA / "time-card-01.xlsx"


def ler_pdf(caminho_pdf):
    leitor = PdfReader(caminho_pdf)
    resultados = []

    for numero_pagina, pagina in enumerate(leitor.pages, start=1):
        texto = pagina.extract_text() or ""

        dados = extrair_cartao_ponto(
            texto,
            numero_pagina
        )

        resultados.append(dados)

    return resultados


def gerar_planilha(resultados):
    PASTA_SAIDA.mkdir(exist_ok=True)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Cartão de Ponto"

    sheet.append([
        "Página",
        "Data",
        "Tipo",
        "Horário"
    ])

    for resultado in resultados:
        pagina = resultado["page"]

        for dia in resultado["days"]:
            data = dia["date_raw"]

            for ponto in dia["punches"]:
                sheet.append([
                    pagina,
                    data,
                    ponto["kind"],
                    ponto["time_hhmm"]
                ])

    workbook.save(ARQUIVO_SAIDA)

    print(f"Planilha criada: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    for numero in range(1, 5):
        pdf = Path(f"pdfs/time-card-0{numero}.pdf")
        arquivo = PASTA_SAIDA / f"time-card-0{numero}.xlsx"

        PDF = pdf
        ARQUIVO_SAIDA = arquivo

        dados = ler_pdf(PDF)
        gerar_planilha(dados)