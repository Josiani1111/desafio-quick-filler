import re


# ============================================================
# PAYROLL 01
# ============================================================

PADRAO_SALARIO_01 = re.compile(
    r"SALARIOLIQUIDONOMES\s+([\d.]+,\d{2})"
)

PADRAO_MES_01 = re.compile(
    r"Mês:\s*([a-z]{3}-\d{2})",
    re.IGNORECASE
)


# ============================================================
# PAYROLL 02, 03 e 04
# ============================================================

PADRAO_MES_02 = re.compile(
    r"(\d{2}/\d{4})"
)

PADRAO_VALOR = re.compile(
    r"^-?\d{1,3}(?:\.\d{3})*,\d{2}$"
)


def extrair_payroll(texto, numero_pagina):

    linhas = [
        linha.strip()
        for linha in texto.splitlines()
        if linha.strip()
    ]

    resultados = []
    mes_atual = ""


    # ========================================================
    # PAYROLL 01
    # ========================================================

    for linha in linhas:

        encontrado_mes = PADRAO_MES_01.search(linha)

        if encontrado_mes:
            mes_atual = encontrado_mes.group(1)

        encontrados = PADRAO_SALARIO_01.findall(linha)

        for valor in encontrados:

            resultados.append({
                "pagina": numero_pagina,
                "mes": mes_atual,
                "linha": linha,
                "salario_liquido": valor
            })


    # ========================================================
    # PAYROLL 02, 03 e 04
    # ========================================================

    for i, linha in enumerate(linhas):

        encontrado_mes = PADRAO_MES_02.search(linha)

        if encontrado_mes:
            mes_atual = encontrado_mes.group(1)

        if "Proventos Líquidos:" in linha:

            if re.search(
                r"Proventos Líquidos:\s*-?\d",
                linha
            ):
                continue

            valores = []

            for proxima in linhas[i + 1:]:

                if PADRAO_VALOR.fullmatch(proxima):

                    valores.append(proxima)

                    if len(valores) == 3:
                        break

            if len(valores) == 3:

                resultados.append({
                    "pagina": numero_pagina,
                    "mes": mes_atual,
                    "linha": linha,
                    "salario_liquido": valores[0]
                })


    # ========================================================
    # PAYROLL 03
    # ========================================================

    for linha in linhas:

        encontrado_mes = re.search(
            r"Período\s*:\s*(\d{2}/\d{4})",
            linha
        )

        if encontrado_mes:
            mes_atual = encontrado_mes.group(1)

        encontrado_liquido = re.search(
            r"Líqüido\s+(-?[\d.]+,\d{2})",
            linha
        )

        if encontrado_liquido:

            resultados.append({
                "pagina": numero_pagina,
                "mes": mes_atual,
                "linha": linha,
                "salario_liquido": encontrado_liquido.group(1)
            })


    # ========================================================
    # PAYROLL 04 - OCR
    # ========================================================

        # ========================================================
    # PAYROLL 04 - OCR
    # ========================================================

    meses_ocr = {
        "JANEIRO": "01",
        "FEVEREIRO": "02",
        "MARÇO": "03",
        "MARCO": "03",
        "ABRIL": "04",
        "MAIO": "05",
        "JUNHO": "06",
        "JULHO": "07",
        "AGOSTO": "08",
        "SETEMBRO": "09",
        "ETEMBRO": "09",
        "OUTUBRO": "10",
        "UTUBRO": "10",
        "NOVEMBRO": "11",
        "IOVEMBRO": "11",
        "DEZEMBRO": "12",
        "EZEMBRO": "12",
        "ANETRO": "01",
    }

    # Primeiro encontramos o mês correto do holerite.
    # Isso evita confundir a data do documento (20/10/2022)
    # com o mês do pagamento.

    for linha in linhas:

        encontrado_mes = re.search(
            r"(JANEIRO|FEVEREIRO|MARÇO|MARCO|ABRIL|MAIO|JUNHO|JULHO|AGOSTO|"
            r"SETEMBRO|ETEMBRO|OUTUBRO|UTUBRO|NOVEMBRO|IOVEMBRO|DEZEMBRO|"
            r"EZEMBRO|ANETRO)[^0-9]*(\d{4})",
            linha,
            re.IGNORECASE
        )

        if encontrado_mes:

            nome_mes = encontrado_mes.group(1).upper()
            ano = encontrado_mes.group(2)

            mes_atual = meses_ocr[nome_mes] + "/" + ano

            break


    # Agora procuramos o líquido a receber.

    liquidos_ocr = []

    for linha in linhas:

        encontrado_liquido = re.search(
            r"L[IÍ]QUI[Dd]O\s+A\s+RECEBER\s+(-?[\d.]+,\d{2})",
            linha,
            re.IGNORECASE
        )

        if encontrado_liquido:

            valor = encontrado_liquido.group(1)

            if valor not in liquidos_ocr:

                liquidos_ocr.append(valor)

                resultados.append({
                    "pagina": numero_pagina,
                    "mes": mes_atual,
                    "linha": linha,
                    "salario_liquido": valor
                })


    return resultados