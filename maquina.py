import customtkinter
import pyperclip

app = customtkinter.CTk() 
app.title('Gerar chamado e máquina')
app.geometry("700x150")


# patrimonio = input('Digite o patrimônio: ')
# sala_laboratorio = input('Digite a sala ou laboratório: ')
# descrição = input('Descreva o ocorrido: ')
# sala = input('Sala ou Lab: 1/2')
# if sala == '1':
#     sala = 'na sala'
# elif sala == '2':
#     sala = 'no laboratório'


# 

# print(final)

def button_callback():

    global sala_lab
    sala_lab = ''
    if check_var.get() == 1 and check_var1.get() == 1:
        sala_lab = 'NA SALA E NO LABORATÓRIO DE '
    elif check_var.get() == 1:
        sala_lab = 'NA SALA '
    elif check_var1.get() == 1:
        sala_lab = 'NO LABORATÓRIO DE '


    texto_final = f'PREZADO(A), GOSTARIA DE INFORMAR QUE O COMPUTADOR IDENTIFICADO PELO PATRIMÔNIO {getpatrimonio.get()}, LOCALIZADO {sala_lab}{getLabOuSala.get()}, APRESENTOU UM {getProblem.get()}. A MÁQUINA FOI RECOLHIDA PARA MANUTENÇÃO E AGORA ENCONTRA-SE EM PLENO FUNCIONAMENTO. JÁ FOI DEVOLVIDA AO LOCAL DE ORIGEM.'

    bloquinho_texto.configure(state='normal')
    bloquinho_texto.delete(0, customtkinter.END)
    bloquinho_texto.insert(0, texto_final)
    bloquinho_texto.configure(state='readonly')
    
def copiar_texto():
    texto_copiado = bloquinho_texto.get()
    pyperclip.copy(texto_copiado)
    print("Texto copiado para a área de transferência!")


labelPatrimonio = customtkinter.CTkLabel(app, text='Patrimônio: ')
labelLabOuSala = customtkinter.CTkLabel(app, text='Sala / Laboratório: ')
labelProblem = customtkinter.CTkLabel(app, text='Problema: ')
getpatrimonio = customtkinter.CTkEntry(app)
getLabOuSala = customtkinter.CTkEntry(app)
getProblem = customtkinter.CTkEntry(app)

check_var = customtkinter.IntVar()
check_var1 = customtkinter.IntVar()



checkboxSala = customtkinter.CTkCheckBox(app, text="SALA", variable=check_var).grid(row=0, column=2)
checkboxLab = customtkinter.CTkCheckBox(app, text="LAB", variable=check_var1).grid(row=1, column=2)


button = customtkinter.CTkButton(app, text="GERAR TEXTO", command=button_callback)
botao_copiar = customtkinter.CTkButton(app, text="Copiar Texto", command=copiar_texto).grid(row=1, column=7, pady=5, padx=5)


bloquinho_texto = customtkinter.CTkEntry(app, width=300)
bloquinho_texto.grid(row=0, column=7, pady=5, padx=5)


getpatrimonio.grid(row=0, column=1, padx=5, pady=5)
getLabOuSala.grid(row=1, column=1, padx=5, pady=5)
getProblem.grid(row=2, column=1, padx=5, pady=5)

labelLabOuSala.grid(row=1, column=0, pady=5, padx=5)
labelPatrimonio.grid(row=0, column=0, pady=5, padx=5)
labelProblem.grid(row=2, column=0, pady=5, padx=5)


button.grid(row=10, column=1, padx=5, pady=5)

app.mainloop()