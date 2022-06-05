from programa.algoritmo.leitura import *

def menu():
    print("-Escolha uma das opções no menu-")
    escolha = int(input("1-Verificar palavra\n2-Finalizar execução\n"))

    if(escolha == 1):
        lerArquivo()

    # elif(escolha == 2):
    #     palavra = int(input("Informe a palavra:\n"))

    else:
        print("finalizando execução")

