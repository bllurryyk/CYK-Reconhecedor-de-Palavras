def cyk(gramatica, s_terminais, s_variaveis, s_inicial, c_regras):
    # algumas impressões temporárias para acompanhar o funcionamento do código
    print(s_terminais)
    print(s_variaveis)
    print(s_inicial)
    print(c_regras)

    # Leitura da palavra
    palavra = str(input("Informe a palavra que deseja testar: "))
    n = 0
    m = len(c_regras)
    tabela = []
    tabela0 = []
    # Separando a palavra dentro de uma lista
    for letra in palavra:
        n += 1
        print(letra)
        sep_palavra = letra
        l = tabela0.append(sep_palavra)
    unindo = tabela.append(tabela0)
    print(tabela)

    
    # mais testes de lógica
    # tabela = [["a", "b"], [0, 0], [0, 0], [0, 0], ["S", 0]]

    # print(c_regras[1][1])
    
    # print(len((s_terminais)))
    div("Executando cyk")
    tabela1 = []
    for j in range(n):
        for i in range(m):
            if(tabela[0][j] in c_regras[i][1]):
                add = tabela1.append(c_regras[i][0])

    unindo = tabela.append(tabela1)
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