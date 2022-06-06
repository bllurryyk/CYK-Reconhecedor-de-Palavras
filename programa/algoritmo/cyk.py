def cyk(gramatica, s_terminais, s_variaveis, s_inicial, c_regras):
    print(s_terminais)
    print(s_variaveis)
    print(s_inicial)
    print(c_regras)

    indice = 0

    # Alguns testes de lógica
    # if(s_terminais[1][0] == "a"):
    #     print("foi")
    #     print(s_terminais[0][1])
    # else:
    #     print("não foi")
    #     print(s_terminais[1][0])

    # Recebendo palavra e definindo o valor de N
    palavra = str(input("Informe a palavra que deseja testar: "))
    n = 0
    m = len(c_regras)
    tabela = []
    tabela0 = []
    for letra in palavra:
        n += 1
        print(letra)
        sep_palavra = letra
        l = tabela0.append(sep_palavra)
    unindo = tabela.append(tabela0)
    print(tabela)

    div("Executando cyk")
    # mais testes de lógica
    # tabela = [["a", "b"], [0, 0], [0, 0], [0, 0], ["S", 0]]

    # print(c_regras[1][1])
    
    # print(len((s_terminais)))
    tabela1 = []
    for j in range(n):
        for i in range(m):
            if(tabela[0][j] in c_regras[i][1]):
                add = tabela1.append(c_regras[i][0])
        # for letra in s_terminais:
        #     print(letra)
        # #    if(s_terminais[letra])
    unindo = tabela.append(tabela1)
    print(tabela)




    # if(tabela[n][0] == "S"):
    #     print("Palava aceita")

    # else:
    #     print("Palavra rejeitada")


def div(nome):
    print('-'*20)
    print(nome)
    print('-'*20)