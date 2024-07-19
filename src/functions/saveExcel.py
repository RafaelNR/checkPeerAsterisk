
import pandas as pd
import os

def saveExcel(filename,  dados):
  
  df = pd.DataFrame(dados)

  # Salvando o DataFrame em um arquivo Excel
  path = os.path.join("./relatorios",f"{filename}.xlsx")
  df.to_excel(path, index=False)

  print(f"Arquivo do Excel criado com sucesso, com nome: {filename}")