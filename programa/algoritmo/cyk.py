def cyk(gramatica, s_terminais, s_variaveis, s_inicial, c_regras):
    print(s_terminais)
    print(s_variaveis)
    print(s_inicial)
    print(c_regras)

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
    for letra in palavra:
        n += 1

    div("Executando cyk")
    # mais testes de lógica
    tabela = [["a", "b"], [0, 0], [0, 0], [0, 0], ["S", 0]]

    # for j in range(n):
    #     if()




    if(tabela[n][0] == "S"):
        print("Palava aceita")

    else:
        print("Palavra rejeitada")


def div(nome):
    print('-'*20)
    print(nome)
    print('-'*20)