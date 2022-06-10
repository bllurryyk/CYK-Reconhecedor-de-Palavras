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

    # Segundo loop
    for i in range(2, n+1):
        for j in range(n-i+1):
            cont = 1
            for k in range(i-1):
                # tabela para comparação
                templist = ['']
                # Garantindo que ele não irá armazenar algo além da regra
                if(tabela[cont][j] != "-"):
                    templist[0] += tabela[cont][j]
                if(tabela[i-cont][j+cont] != "-"):
                    templist[0] += tabela[i-cont][j+cont]
                # Passando por cada regra e vendo se bate com a nossa lista temporaria
                for c in range(m):
                    if(templist[0] == c_regras[c][1]):
                        if(tabela[i][j] == "-"):
                            tabela[i][j] = c_regras[c][0]
                cont += 1
            cont = 1

    # Verificação da palavra
    if(tabela[n][0] == "S"):
        print("Palava aceita")
        div("Tabela Final")
    else:
        print("Palavra rejeitada")
    ll = 0
    for linha in tabela:
        print(tabela[ll])
        ll += 1

def div(nome):
    print('-'*20)
    print(nome)
    print('-'*20)