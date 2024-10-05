import os
from tkinter import messagebox

def agendar_desligamento(horas, minutos, botão):
    try:
        total_segundos = horas * 3600 + minutos * 60
        comando = f"shutdown /s /t {total_segundos}"
        os.system(comando)

        messagebox.showinfo("Desligamento Agendado", f"O computador será desligado em {horas} horas e {minutos} minutos.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um numero válido.")