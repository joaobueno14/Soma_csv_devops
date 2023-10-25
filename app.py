import tkinter as tk
from tkinter import filedialog
import pandas as pd

def remover_coluna_id_e_calcular_somas():
    arquivo_csv = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if arquivo_csv:
        # Carrega o CSV em um DataFrame do pandas
        df = pd.read_csv(arquivo_csv)

        # Verifica se a coluna 'ID' existe no DataFrame antes de removê-la
        if 'ID' in df.columns:
            # Remove a coluna 'ID'
            df = df.drop(columns=['ID'])

            # Calcula as somas separadas das colunas "Original Estimate" e "Completed Work" como inteiros
            soma_original_estimate = int(df['Original Estimate'].sum())
            soma_completed_work = int(df['Completed Work'].sum())

            resultado_label.config(text=f"Coluna 'ID' removida com sucesso.\n"
                                         f"Soma 'Original Estimate': {soma_original_estimate}\n"
                                         f"Soma 'Completed Work': {soma_completed_work}")
        else:
            resultado_label.config(text="A coluna 'ID' não foi encontrada no arquivo CSV.")

# Configura a interface gráfica
root = tk.Tk()
root.title("Remoção da Coluna 'ID' e Cálculo de Somas")

# Define a geometria da janela (largura x altura)
root.geometry("300x200")

# Altera o texto do botão
remover_id_button = tk.Button(root, text="Selecionar arquivo CSV", command=remover_coluna_id_e_calcular_somas)
remover_id_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()
