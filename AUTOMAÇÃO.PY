''' Automação inicante 
 Esse projeto é uma aplicação simples que mescla arquivos e utilizando imports, 
e organizando os arquivos 
'''
# Iniciamos usando uma biblioteca chamada PyPDF2 
# Usando merge() , ferramenta que se usa pra mesclar 
# Usando listdir() , listando o que tem dentro da nossa pasta 
# Usando sort(), ordena o nosso arquivo.

import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf"in arquivo:
         merger.append("aquivos/{arquivo}") 
merger .white("PDF Final.pdf")

# ORGANIZAÇÃO DO NOSSO DADOS 

import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais= {"imagens" [".png",".jpg"],
         "pdfs"[".pdf"],        
}

for arquivo in lista_arquivos:
    nome,extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais['pasta']:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
