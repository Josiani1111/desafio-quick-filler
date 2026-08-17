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
    r"-?\d{1,3}(?:\.\d{3})*,\d{2}"
)


def extrair_payroll(texto, numero_pagina):

    linhas = [
        linha.strip()
        for linha in texto.splitlines()
        if linha.strip()
    ]

    resultados = []


    # ========================================================
    # PAYROLL 01
    # ========================================================

    mes_atual = ""

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

    mes_atual = ""

    for i, linha in enumerate(linhas):

        # Descobre o mês
        encontrado_mes = PADRAO_MES_02.search(linha)

        if encontrado_mes:
            mes_atual = encontrado_mes.group(1)


        # Procura Proventos Líquidos
        if "Proventos Líquidos:" not in linha:
            continue


        # Ignora o bloco ACERTO
        #
        # Exemplo:
        # Proventos Líquidos:-1,04
        #
        if "Proventos Líquidos:-" in linha:
            continue


        # Procura os valores seguintes
        valores = []

        for proxima in linhas[i + 1:]:

            if PADRAO_VALOR.fullmatch(proxima):

                valores.append(proxima)

                if len(valores) == 3:
                    break


        # Primeiro valor = Proventos Líquidos
        if len(valores) == 3:

            resultados.append({
                "pagina": numero_pagina,
                "mes": mes_atual,
                "linha": linha,
                "salario_liquido": valores[0]
            })


    return resultados