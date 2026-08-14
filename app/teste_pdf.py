from pypdf import PdfReader
from parser import extrair_cartao_ponto


caminho = "uploads/desafios Quick Filler - Copia.pdf"

leitor = PdfReader(caminho)

print("Quantidade de páginas:", len(leitor.pages))

print("\n=== TESTANDO NOVO PARSER ===")


for numero, pagina in enumerate(leitor.pages, start=1):

    texto = pagina.extract_text()

    resultado = extrair_cartao_ponto(texto, numero)

    print(f"\n--- PÁGINA {numero} ---")
    print("Quantidade de dias:", len(resultado["days"]))

    for dia in resultado["days"]:
        print(dia)