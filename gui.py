import tkinter as tk
from logica import agendar_desligamento

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Angendar Desligamento")

    janela.iconbitmap('power.ico')

    janela.resizable(False, False)

    janela.attributes('-topmost', True)

    janela.configure(bg='black')

    tk.Label(janela, text="Horas:", bg='black', fg='white').grid(row=0, column=0)
    spinbox_horas = tk.Spinbox(janela, from_=0, to=23, width=5)
    spinbox_horas.grid(row=0, column=1)

    tk.Label(janela, text="Minutos:", bg='black', fg='white').grid(row=1, column=0)
    spinbox_minutos = tk.Spinbox(janela, from_=0, to=59, width=5)
    spinbox_minutos.grid(row=1, column=1)

    botao = tk.Button(janela, width=10, height=1, text="Agendar")
    botao.grid(row=2, column=0, columnspan=2)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()