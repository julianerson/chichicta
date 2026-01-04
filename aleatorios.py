import random
import inquirer
#vc tem dado em casa?
def dado():
    dado = int(input("escreva o numero de lados do dado"))
    while True:
        oi = random.randint(1,dado)
        inter = input("quer lançar o dado s/n")
        if inter == "s":
            print(oi)
            continue
        elif inter == "n":
            break 
        else:
            print(oi)
            continue
#aleatoriedades
def alea():
    i= input("escreva palavras")
    i = i.split()
    while True:
        u = random.choice(i)
        fs = input("pressione emter ou n")
        #parte nescessaria para n quebrar o codigo
        if fs == "n":
            break
        else:
            print(u)
            continue
#parte do questionario
pergunta = [
        inquirer.List(
            "size",
            message = "que tu quer",
            choices = ["dado", "alea", "sair"]
            )]
#o loop final
while True:
    #pergunta
    res = inquirer.prompt(pergunta)
    #opçoes
    if "sair" in str(res):
        break
    elif "dado" in str(res):
        dado()
        continue
    elif "alea" in str(res):
        alea()
        continue

