import pandas as pd

Vendas_df = pd.read_excel("Pandas\Vendas.xlsx")

#fatoramento por loja

fatoramento = Vendas_df["ID Loja"]
pd.set_option('display.max_columns' , None)

print(fatoramento)



#tudo que tem relação com pandas ta no google colab