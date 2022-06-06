from programa.algoritmo.cyk import cyk

def lerArquivo():
    with open('arquivos/gramatica.txt', 'r') as gramatica:
        gramatica = gramatica.read().splitlines()
    div("Carregado a seguinte gramática")
    print(gramatica)

    # G = (V, T, P, S)
    # gramatica = (s_variaveis, s_terminais, c_regras, s_inicial)
    s_terminais = []
    # Símbolos não-terminais:
    s_variaveis = []
    s_inicial = gramatica[0][0]
    # Conjunto de produções ou regras:
    c_regras = []

    for l in gramatica:
        sep_r, sep_p = l.split(" => ")
        sep_p = sep_p.split(" | ")

        for letra in sep_p:
            c_regras.append([sep_r, letra])
            if not str.islower(letra):
                s_variaveis.append([sep_r, letra])
            if str.islower(letra):
                s_terminais.append([sep_r, letra])

    div("Leitura efetuada com sucesso")
    cyk(gramatica, s_terminais, s_variaveis, s_inicial, c_regras)

def div(texto):
    print('-'*20)
    print(texto)
    print('-'*20)