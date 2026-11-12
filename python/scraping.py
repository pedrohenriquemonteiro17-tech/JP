import pandas as pd

dados = [
    ["2024-09-10", "Gostei das propostas do candidato X"],
    ["2024-09-12", "Não concordo com o candidato Y"],
    ["2024-09-13", "Debate presidencial aconteceu hoje"]
]

df = pd.DataFrame(
    dados,
    columns=["data", "texto"]
)

df.to_csv("dados/comentarios.csv", index=False)

print(df)

print("Arquivo criado")