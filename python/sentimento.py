import pandas as pd

df = pd.read_csv("dados/comentarios_tratados.csv")

def sentimento(texto):

    positivas = [
        "gostei",
        "bom",
        "ótimo",
        "excelente"
    ]

    negativas = [
        "ruim",
        "péssimo",
        "não"
    ]

    for palavra in positivas:
        if palavra in texto:
            return "Positivo"

    for palavra in negativas:
        if palavra in texto:
            return "Negativo"

    return "Neutro"

df["sentimento"] = df["texto"].apply(sentimento)

df.to_csv("dados/comentarios_classificados.csv", index=False)

print("Sentimentos classificados")