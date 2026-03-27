import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados.csv")

df["faturamento"] = df["preco"] * df["quantidade"]

df = df.sort_values(by="faturamento", ascending=False)

print(df)

df.to_csv("vendas_tratadas.csv", index=False)

plt.figure()
plt.bar(df["produto"], df["faturamento"])
plt.title("Faturamento por Produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento")
plt.xticks(rotation=45)

plt.show()
