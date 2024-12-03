import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt


#titulo
st.write("""
# Analise de preços dos carros mais usados no brasil (2021 - 2023)
    Analisamos um dataset com a tabela fipe de diversos modelos de 
    carros entre os anos de 2021 até 2023, e usando nosso conhecimento no 
    Mathplotlib, produzimos gráficos fazendo comparações para facilitar 
    a visualição do aumento e queda dos preços de diversos veículos. 
""")


#--------------------------marcas mais populares---------------------------------------------
st.write("- Marcas mais Populares no Brasil")
selec = pd.read_excel('./marcaSelec.xlsx')

for carro in selec['brand'].unique():
  df_carro = selec.loc[selec['brand'] == carro]

  plt.plot(df_carro['year_of_reference'], df_carro['year_mean'], marker='o', label=carro)

  plt.title('Variação média anual na fipe')
  plt.xlabel('Ano')
  plt.ylabel('Preço (R$)')

  plt.xticks([2021, 2022, 2023])
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.grid(True)

st.pyplot(plt)
plt.clf()
#-------------------------------------------------------------------------------------------


#---------------------Comparação com modelos populares no brasil----------------------------
st.write("- Comparando modelos populares do Brasil")
selec = pd.read_excel('./carrosSelec.xlsx')

for carro in selec['full_name'].unique():
  df_carro = selec.loc[selec['full_name'] == carro]

  plt.plot(df_carro['year_of_reference'], df_carro['year_mean'], marker='o', label=carro)

  plt.title("Comparação entre os modelos populares no brasil")
  plt.xlabel('Ano')
  plt.ylabel('Preço (R$)')

  plt.xticks([2021, 2022, 2023])
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.grid(True)

st.pyplot(plt)
plt.clf()
#-------------------------------------------------------------------------------------------


#-----------------------Comparação como os tipos de combustivel-----------------------------
st.write("- Comparação como os tipos de combustivel")
selec = pd.read_excel('./mediaFuel.xlsx')

for carro in selec['fuel'].unique():
  df_carro = selec.loc[selec['fuel'] == carro]

  plt.plot(df_carro['year_of_reference'], df_carro['year_mean'], marker='o', label=carro)

  plt.title("Comparação entre os tipos de combustivel")
  plt.xlabel('Ano')
  plt.ylabel('Preço (R$)')

  plt.xticks([2021, 2022, 2023])
  plt.legend()
  plt.tight_layout()
  plt.grid(True)

st.pyplot(plt)
plt.clf()
#------------------------------------------------------------------------------------------


#---------------------------Comparação entre os cambios------------------------------------
st.write("- Comparação entre os tipos de cambio")
selec = pd.read_excel('./mediaGear.xlsx')

for carro in selec['gear'].unique():
  df_carro = selec.loc[selec['gear'] == carro]

  plt.plot(df_carro['year_of_reference'], df_carro['year_mean'], marker='o',label = carro)

  plt.title(carro)
  plt.xlabel('Ano')
  plt.ylabel('Preço (R$)')

  plt.xticks([2021, 2022, 2023])
  plt.legend()
  plt.grid(True)

st.pyplot(plt)
plt.clf()
#------------------------------------------------------------------------------------------

