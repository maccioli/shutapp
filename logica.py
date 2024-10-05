import os
from tkinter import messagebox

def agendar_desligamento(horas, minutos, botão):
    try:
        total_segundos = horas * 3600 + minutos * 60
        comando = f"shutdown /s /t {total_segundos}"
        os.system(comando)

        messagebox.showinfo("Desligamento Agendado", f"O computador será desligado em {horas} horas e {minutos} minutos.")

        botao.config(text="Cancelar Agendamento", command=lambda: cancelar_agendamento(botao))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um numero válido.")

def cancelar_agendamento(botao):
    os.system("shutdown /a")
    messagebox.showinfo("Agendamento Cancelado", "O agendamento foi cancelado.")

    botao.config(text="Agendar", command=lambda: botao.event_generate("<<Agendar>>"))