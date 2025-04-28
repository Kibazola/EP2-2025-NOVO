#1
from random import randint

def rolar_dados(n):
    resultado = []
    i = 0
    while i < n:
        resultado.append(randint(1,6))

        i+=1
    return resultado

#2
def guardar_dado(dados_r, dados_g, num):
    dados_g.append(dados_r[num])
    del dados_r[num]
    resposta = [dados_r, dados_g]
    return resposta

#3
def remover_dado(dados_rolados, dados_no_estoque,dado_para_remover):
    dados_rolados_novo = dados_rolados.copy()
    dados_rolados_novo.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque_novo = dados_no_estoque.copy()
    dados_no_estoque_novo.pop(dado_para_remover)

    novo = [dados_rolados_novo,dados_no_estoque_novo]

    return novo

#4
def calcula_pontos_regra_simples(lista_n):
    dic_r = {}
    i = 1
    while i < 7:
        soma = 0
        for numero in lista_n:
            if numero == i:
                soma += numero
        dic_r[i] = soma
        i += 1
    return dic_r
