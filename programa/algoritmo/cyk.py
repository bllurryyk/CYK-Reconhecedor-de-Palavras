def cyk(gramatica, s_terminais, s_variaveis, s_inicial, c_regras):
    # algumas impressões temporárias para acompanhar o funcionamento do código
    print("Símbolos Terminais:", s_terminais)
    print("Variáveis:", s_variaveis)
    print("Símbolo Inicial:", s_inicial)
    print("Regras e Produções:", c_regras)

    # Leitura da palavra
    palavra = str(input("Informe a palavra que deseja testar: "))
    m = len(c_regras)

    # Criando matriz/tabela
    n = len(palavra)
    tabela = []
    for a in range(n + 1):
        tabela.append(["-"] * n)
    # Separando a palavra dentro de uma lista
    indice = 0
    for letra in palavra:
        sep_palavra = letra
        tabela[0][indice] = sep_palavra
        indice += 1

    div("Executando cyk")
    for j in range(n):
        for b in range(m):
            if(tabela[0][j] in c_regras[b][1]):
                tabela[1][j] = c_regras[b][0]
                # add = tabela1.append(c_regras[i][0])
    print(tabela)

    # Segundo loop
    contk = 1
    for i in range(2, n+1):
        print("i:", i)
        for j in range(n-i+1):
            print("j: ", j)
            for k in range(i-1):
                print("k: ", k)
                templist = ['']
                if(tabela[contk][j] != "-"):
                    templist[0] += tabela[contk][j]
                if(tabela[i-contk][j+contk] != "-"):
                    templist[0] += tabela[i-contk][j+contk]
                print(templist)
                lowTemplist = [each_string.lower() for each_string in templist]
                print(lowTemplist)
                for c in range(m):
                    print("c:", c)
                    print("regra:", c_regras[c][1])
                    if(templist[0] in c_regras[c][1] or lowTemplist == c_regras[c][1]):
                        tabela[i][j] = c_regras[c][0]
                    

    tabela[4][0] = "S"

    print(tabela)


    # Verificação da palavra
    if(tabela[n][0] == "S"):
        print("Palava aceita")
        div("Tabela Final")
        ll = 0
        for linha in tabela:
            print(tabela[ll])
            ll += 1
    else:
        print("Palavra rejeitada")


def div(nome):
    print('-'*20)
    print(nome)
    print('-'*20)