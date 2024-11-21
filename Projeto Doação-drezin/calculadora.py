import tkinter as tk
from tkinter import messagebox

def calcular(operacao):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                mensagem.set("Erro: divisão por zero")
                return
            resultado = num1 / num2
        
        mensagem.set(f"Resultado: {resultado:.2f}")
    except ValueError:
        mensagem.set("Erro: insira números válidos")

def limpar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    mensagem.set("")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Gráfica")
janela.geometry("300x300")

# Campo de entrada para o primeiro número
tk.Label(janela, text="Número 1:").pack(pady=5)
entry1 = tk.Entry(janela)
entry1.pack()

# Campo de entrada para o segundo número
tk.Label(janela, text="Número 2:").pack(pady=5)
entry2 = tk.Entry(janela)
entry2.pack()

# Botões para as operações
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="+", width=5, command=lambda: calcular('+')).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="-", width=5, command=lambda: calcular('-')).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="×", width=5, command=lambda: calcular('*')).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="÷", width=5, command=lambda: calcular('/')).grid(row=0, column=3, padx=5)

# Área de mensagem para o resultado
mensagem = tk.StringVar()
tk.Label(janela, textvariable=mensagem, fg="blue").pack(pady=10)

# Botão para limpar os campos
tk.Button(janela, text="Limpar", command=limpar).pack(pady=10)

# Iniciando o loop principal da interface
janela.mainloop()