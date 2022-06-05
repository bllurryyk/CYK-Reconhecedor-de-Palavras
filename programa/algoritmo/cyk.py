def lerArquivo():
    gramatica = open('arquivos/gramatica.txt', 'r')
    for line in gramatica:
        print(line)

    print("Leitura efetuada com sucesso")
    cyk(gramatica)

def cyk(gramatica):
    print("Executando cyk")
    gramatica.close()