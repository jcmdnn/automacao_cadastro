import pandas as pd
import robot

# ler arquivo excel
df = pd.read_excel('cadastro_clientes.xlsx')

robot.cadastrar_web(df)
