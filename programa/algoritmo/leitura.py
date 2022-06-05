from programa.algoritmo.cyk import cyk

def lerArquivo():
    gramatica = open('arquivos/gramatica.txt', 'r')

    div()
    print("Leitura efetuada com sucesso")
    cyk(gramatica)

def div():
    print('-'*20)