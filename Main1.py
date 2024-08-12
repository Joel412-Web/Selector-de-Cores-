from tkinter import messagebox
import customtkinter

def atualizar_cor(valor):
    # Obtém os valores dos sliders
    r = int(SVermelho.get())
    g = int(SVerde.get())
    b = int(SAzul.get())
    
    # Atualiza os textos das labels
    LVermelho.configure(text=f'Vermelho {r}')
    LVerde.configure(text=f'Verde {g}')
    LAzul.configure(text=f'Azul {b}')
    
    # Converte os valores RGB para hexadecimal
    cor_hex = f'#{r:02x}{g:02x}{b:02x}'
    
    # Atualiza a cor de fundo do Canvas
    pcor.config(bg=cor_hex)
    
    # Atualiza o valor do campo de entrada com o código hexadecimal
    EHexa.delete(0, customtkinter.END)
    EHexa.insert(0, cor_hex)

# Função para copiar o valor de EHexa
def copiar_hex():
    janela.clipboard_clear()  # Limpa a área de transferência
    janela.clipboard_append(EHexa.get())  # Copia o conteúdo de EHexa
    messagebox.showinfo('Copia','Texto copiado com sucesso !')

def Limpar():
    SVermelho.set(0)
    SVerde.set(0)
    SAzul.set(0)
    LVermelho.configure(text='Vermelho 0')
    LVerde.configure(text='Verde 0')
    LAzul.configure(text='Azul 0')
    EHexa.delete(0, customtkinter.END)
    pcor.config(bg='Black')
    messagebox.showinfo('Valores','Valores Limpos com sucesso !')

def Sair():
    resposta = messagebox.askquestion("Sair", "Deseja sair da aplicação?")
    if resposta == 'yes':  # Se o usuário clicar em "Sim"
        janela.destroy()    

janela = customtkinter.CTk()
janela.geometry('800x280+100+100')
janela.title('Meu Selector de Cores © Dev Joel 2024')
janela.resizable(False, False)

pcor = customtkinter.CTkCanvas(janela)
pcor.config(bg='Black')
pcor.place(x=10, y=10)

LVermelho = customtkinter.CTkLabel(janela, text='Vermelho 0')
LVermelho.place(x=320, y=10)

SVermelho = customtkinter.CTkSlider(janela, width=465, from_=0, to=255, command=atualizar_cor)
SVermelho.place(x=320, y=45)

LVerde = customtkinter.CTkLabel(janela, text='Verde 0')
LVerde.place(x=320, y=70)


SVerde = customtkinter.CTkSlider(janela, width=465, from_=0, to=255, command=atualizar_cor)
SVerde.place(x=320, y=105)

LAzul = customtkinter.CTkLabel(janela, text='Azul 0')
LAzul.place(x=320, y=135)


SAzul = customtkinter.CTkSlider(janela, width=465, from_=0, to=255, command=atualizar_cor)
SAzul.place(x=320, y=170)

EHexa = customtkinter.CTkEntry(janela)
EHexa.place(x=10, y=230)

Copiar = customtkinter.CTkButton(janela, text='Copiar', width=85, command=copiar_hex)
Copiar.place(x=155, y=230)
Limpar = customtkinter.CTkButton(janela, text='Limpar', width=85, command=Limpar)
Limpar.place(x=245, y=230)
Sair = customtkinter.CTkButton(janela, text='Sair', width=85, command=Sair)
Sair.place(x=335, y=230)



janela.mainloop()