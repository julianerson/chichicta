import subprocess
import inquirer 
import os
#detecta o sistema operacional e diz por onde deve começar a buscaS
oloco = os.name
if oloco == "nt":
    o = r"C:\Users"
elif oloco == "posix":
    o = r'/storage'
#as opçoes que vc tem
opoes = [inquirer.List("size", message="me diz o que tu quer",choices=["buscar","linha"])]
lolo = inquirer.prompt(opoes)
nome = input("Nome do arquivo: ")
#aqui temos o coraçao do codigo
for raiz, pastas, arquivos in os.walk(o):#raiz=nome do camino onde a pasta esta procrando, pasta = nome das subpastas dentro de pasta, arquivos =lista de arquivos em pasta
    for arquivo in arquivos:#olha cada arquivo em arquivos
        if nome.lower() in arquivo.lower():#checa se o aquivo e o que queremos
            resultado = os.path.join(raiz, arquivo)#ACHOU
#obs ele so ve o primeiro nome que bate


if not resultado: #<=== ativa se o caminho nao existir
    print(f"Arquivo '{nome}' não encontrado.")
    exit()

if "linha" in str(lolo):
    # Agora abre o arquivo sem erro

    with open(resultado, 'r', encoding='utf-8', errors='ignore') as arquivo:
     conteudo = arquivo.read()

    texto_procurado = input('o que vc quer achar?')
#ali^ Procura se uma linha ou texto específico existe
    if texto_procurado in conteudo:
        print(f"Encontrado: {texto_procurado}")
    else:#resultado caso nao tiver sexatamente o que vc escreveu
       print("Não encontrado.")# Caminho do seu arquivo (mude para o que você precisa)

# Ou encontrar a linha exata e imprimir as linhas ao redor
    linhas = conteudo.splitlines()
    for i, linha in enumerate(linhas):
           if texto_procurado in linha:
                print(f"Linha {i+1}: {linha}")

elif "buscar" in str(lolo):
    print(resultado)