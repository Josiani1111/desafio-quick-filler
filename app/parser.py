import re


def extrair_cartao_ponto(texto, numero_pagina):
    dias = []

    linhas = texto.splitlines()

    padrao_dia = re.compile(
        r"^\s*(\d{1,2})\s*-\s*(\w{3})"
    )

    padrao_horario = re.compile(
        r"\b\d{2}:\d{2}\b"
    )

    dia_atual = None

    for linha in linhas:

        # Ignora rodapés
        if "Número do processo" in linha:
            break

        if "Número do documento" in linha:
            break

        if "Assinado eletronicamente" in linha:
            break

        resultado = padrao_dia.match(linha)

        if resultado:
            dia, semana = resultado.groups()

            data = f"{dia} - {semana}"

            # Evita criar o mesmo dia duas vezes
            if dias and dias[-1]["date_raw"] == data:
                dia_atual = dias[-1]
                continue

            dia_atual = {
                "date_raw": data,
                "punches": []
            }

            dias.append(dia_atual)

        elif dia_atual:

            horarios = padrao_horario.findall(linha)

            for horario in horarios:

                tipo = (
                    "IN"
                    if len(dia_atual["punches"]) % 2 == 0
                    else "OUT"
                )

                dia_atual["punches"].append({
                    "kind": tipo,
                    "time_raw": horario,
                    "time_hhmm": horario
                })

    return {
        "page": numero_pagina,
        "days": dias
    }