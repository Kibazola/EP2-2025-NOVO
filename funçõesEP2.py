#QUESTÕES DO CONCEITO D:
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
    
#6
def calcula_pontos_sequencia_baixa(lista_n):
    ii = 0
    lista_n2 = []
    while ii < len(lista_n):    
        i = 0
        m = lista_n[0]
        while i < len(lista_n):
            if lista_n[i] <= m:
                m = lista_n[i]
                indice = i
            i += 1
        lista_n2.append(m)
        del lista_n[indice]
        ii = 0
   
    seq = 0
    i = 1
    seq_final = 0
    while i < len(lista_n2):
        if lista_n2[i] - lista_n2[i - 1] == 1:
            seq += 1
            if seq > seq_final:
                seq_final = seq
        elif lista_n2[i] - lista_n2[i - 1] > 1:
            seq = 0
        i += 1
    if seq_final >= 3:
        return 15
    else:
        return 0

#7
def calcula_pontos_sequencia_alta(lista_n):
    ii = 0
    lista_n2 = []
    while ii < len(lista_n):    
        i = 0
        m = lista_n[0]
        while i < len(lista_n):
            if lista_n[i] <= m:
                m = lista_n[i]
                indice = i
            i += 1
        lista_n2.append(m)
        del lista_n[indice]
        ii = 0
   
    seq = 0
    i = 1
    seq_final = 0
    while i < len(lista_n2):
        if lista_n2[i] - lista_n2[i - 1] == 1:
            seq += 1
            if seq > seq_final:
                seq_final = seq
        elif lista_n2[i] - lista_n2[i - 1] > 1:
            seq = 0
        i += 1
    if seq_final >= 4:
        return 30
    else:
        return 0
    
#QUESTÕES DO CONCEITO C:
#8
def calcula_pontos_full_house(lista_n):
    soma = 0
    for num in lista_n:
        soma += num
    
    lista_n2 = []
    for num1 in lista_n:
        if num1 not in lista_n2:
            lista_n2.append(num1)
        else:
            False
    if len(lista_n2) == 2:
        return soma
    else:
        return 0

#9
def calcula_pontos_quadra(lista_n):
    soma = 0
    for num in lista_n:
        soma += num
    
    maior_ig = 0
    for num1 in lista_n:
        ig = 0
        for num2 in lista_n:
            if num1 == num2: 
                ig += 1
        if ig > maior_ig:
            maior_ig = ig
    if maior_ig >= 4:
        return soma
    else:
        return 0
#QUESTÕES DO CONCEITO B:
#10
def calcula_pontos_quina(lista):
    novo = []
    for n in lista:
        if n not in novo:
            novo.append(n)
            c = lista.count(n)
            if c >= 5:
                return 50      
    return 0

# 11
#11.1
def calcula_pontos_quina(lista):
    novo = []
    for n in lista:
        if n not in novo:
            novo.append(n)
            c = lista.count(n)
            if c >= 5:
                return 50     
    return 0
#11.2
def calcula_pontos_full_house(lista_n):
    soma = 0
    for num in lista_n:
        soma += num

    lista_n2 = []
    for num1 in lista_n:
        if num1 not in lista_n2:
            lista_n2.append(num1)

    if len(lista_n2) == 2:
        num_a = lista_n2[0]
        num_b = lista_n2[1]

        cont_a = 0
        cont_b = 0

        for num in lista_n:
            if num == num_a:
                cont_a += 1
            elif num == num_b:
                cont_b += 1

        if (cont_a == 3 and cont_b == 2) or (cont_a == 2 and cont_b == 3):
            return soma
        else:
            return 0
    else:
        return 0
#11.3
def calcula_pontos_quadra(lista_n):
    soma = 0
    for num in lista_n:
        soma += num
    maior_ig = 0
    for num1 in lista_n:
        ig = 0
        for num2 in lista_n:
            if num1 == num2: 
                ig += 1
        if ig > maior_ig:
            maior_ig = ig
    if maior_ig >= 4:
        return soma
    else:
        return 0
#11.4
def calcula_pontos_soma(lista_n):
    soma +=0
    for n in lista_n:
        soma+=n
    return soma
#11.5
def calcula_pontos_sequencia_alta(lista_n):
        lista_n = lista_n.copy()
        ii = 0
        lista_n2 = []
        while ii < len(lista_n):    
            i = 0
            m = lista_n[0]
            while i < len(lista_n):
                if lista_n[i] <= m:
                    m = lista_n[i]
                    indice = i
                i += 1
            lista_n2.append(m)
            del lista_n[indice]
            ii = 0
    
        seq = 0
        i = 1
        seq_final = 0
        while i < len(lista_n2):
            if lista_n2[i] - lista_n2[i - 1] == 1:
                seq += 1
                if seq > seq_final:
                    seq_final = seq
            elif lista_n2[i] - lista_n2[i - 1] > 1:
                seq = 0
            i += 1
        if seq_final >= 4:
            return 30
        else:
            return 0
#11.6
def calcula_pontos_sequencia_baixa(lista_n):
    ii = 0
    lista_n2 = []
    while ii < len(lista_n):    
        i = 0
        m = lista_n[0]
        while i < len(lista_n):
            if lista_n[i] <= m:
                m = lista_n[i]
                indice = i
            i += 1
        lista_n2.append(m)
        del lista_n[indice]
        ii = 0
   
    seq = 0
    i = 1
    seq_final = 0
    while i < len(lista_n2):
        if lista_n2[i] - lista_n2[i - 1] == 1:
            seq += 1
            if seq > seq_final:
                seq_final = seq
        elif lista_n2[i] - lista_n2[i - 1] > 1:
            seq = 0
        i += 1
    if seq_final >= 3:
        return 15
    else:
        return 0


#11.7
def calcula_pontos_regra_avancada(entrada):
    dicionário = {}

    
        
    dicionário['cinco_iguais'] = calcula_pontos_quina(entrada)
    dicionário['full_house'] = calcula_pontos_full_house(entrada)
    dicionário['quadra'] = calcula_pontos_quadra(entrada)
    dicionário['sem_combinacao'] = calcula_pontos_soma(entrada)
    dicionário['sequencia_alta'] = calcula_pontos_sequencia_alta(entrada)
    dicionário['sequencia_baixa'] = calcula_pontos_sequencia_baixa(entrada)


    return dicionário

#12
def calcula_pontos_regra_simples(lista_n):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    for n in lista_n:
        dic[n] += n

    return dic

   
def faz_jogada(dados, categoria, cartela_de_pontos):

    for regra, dic in cartela_de_pontos.items():
        if regra == "regra_simples":

            
            if categoria in ["1","2","3","4","5","6"]:
                categoria = int(categoria)

                if categoria in dic:
                    cartela_de_pontos["regra_simples"][categoria] = calcula_pontos_regra_simples(dados)[categoria]

        elif regra == "regra_avancada":
            if categoria in dic:
                cartela_de_pontos["regra_avancada"][categoria] = calcula_pontos_regra_avancada(dados)[categoria]


    return cartela_de_pontos
