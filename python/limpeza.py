import pandas as pd
import re

df = pd.read_csv("dados/comentarios.csv")

def limpar(texto):

    texto = texto.lower()

    texto = re.sub(r'[^a-zA-ZÀ-ÿ0-9 ]', '', texto)

    return texto

df["texto"] = df["texto"].apply(limpar)

df.to_csv("dados/comentarios_tratados.csv", index=False)

print("Limpeza concluída")