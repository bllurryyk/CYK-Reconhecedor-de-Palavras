def cyk(gramatica, s_terminais, s_variaveis, s_inicial, c_regras):
    # algumas impressões temporárias para acompanhar o funcionamento do código
    print(s_terminais)
    print(s_variaveis)
    print(s_inicial)
    print(c_regras)

    

    # Leitura da palavra
    palavra = str(input("Informe a palavra que deseja testar: "))
    m = len(c_regras)

    # Criando matriz/tabela
    n = len(palavra)
    print(n)
    tabela = []
    for i in range(n + 1):
        tabela.append([0] * 4)
    # Separando a palavra dentro de uma lista
    indice = 0
    for letra in palavra:
        print(letra)
        sep_palavra = letra
        tabela[0][indice] = sep_palavra
        print("indice: ", indice)
        indice += 1
    print(tabela)

    
    # mais testes de lógica
    # tabela = [["a", "b"], [0, 0], [0, 0], [0, 0], ["S", 0]]

    # print(c_regras[1][1])
    
    # print(len((s_terminais)))
    div("Executando cyk")
    for j in range(n):
        for i in range(m):
            if(tabela[0][j] in c_regras[i][1]):
                tabela[1][j] = c_regras[i][0]
                # add = tabela1.append(c_regras[i][0])
    print(tabela)



    # Verificação da palavra
    # if(tabela[n][0] == "S"):
    #     print("Palava aceita")

    # else:
    #     print("Palavra rejeitada")


def div(nome):
    print('-'*20)
    print(nome)
    print('-'*20)