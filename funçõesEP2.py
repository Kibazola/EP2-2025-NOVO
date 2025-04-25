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