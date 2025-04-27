from random import randint

def rolar_dados(n):
    resultado = []
    i = 0
    while i < n:
        resultado.append(randint(1,6))

        i+=1
    return resultado




#Terceira função:

def remover_dado(dados_rolados, dados_no_estoque,dado_para_remover):
    dados_rolados_novo = dados_rolados.copy()
    dados_rolados_novo.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque_novo = dados_no_estoque.copy()
    dados_no_estoque_novo.pop(dado_para_remover)

    novo = [dados_rolados_novo,dados_no_estoque_novo]

    return novo