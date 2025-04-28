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

#5
def calcula_pontos_soma(lista_n):
    i = 1
    seq = 0
    seq_final = 0
    ig = 0
    sem = 0
    soma = 0
    for num in lista_n:
        soma += num
    while i < len(lista_n):
        if lista_n[i] - lista_n[i - 1] == 1:
            seq += 1
            if seq > seq_final:
                seq_final = seq
        elif lista_n[i] == lista_n[i - 1]:
            ig =+ 1
            if ig > sem:
                sem = ig
        else:
            seq = 0
        i += 1
    if sem >= 5:
        return 50
    elif seq_final == 4:
        return 15
    elif seq_final == 5:
        return 30
    else:
        return soma