def menu():
    print("-Escolha uma das opções no menu-")
    escolha = int(input("1-Ler arquivo de texto\n2-Verificar palavra\n3-Finalizar execução\n"))

    if(escolha == 1):
        print("lendo arquivo")

    elif(escolha == 2):
        palavra = int(input("Informe a palavra:\n"))

    else:
        print("finalizando execução")

from algoritmo.cyk import cyk