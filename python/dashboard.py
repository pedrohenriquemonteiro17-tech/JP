import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/comentarios_classificados.csv")

contagem = df["sentimento"].value_counts()

plt.figure(figsize=(8,5))

contagem.plot(
    kind="bar",
    color=["green","red","blue"]
)

plt.title("Distribuição dos Sentimentos")

plt.savefig("graficos/sentimentos.png")

plt.show()