<<<<<<< HEAD
import funcoes

cartela_de_pontos = {
    'regra_simples':  {
        1:"  ",
        2:"  ",
        3:"  ",
        4:"  ",
        5:"  ",
        6:"  "
    },
    'regra_avancada' : {
        'sem_combinacao':"  ",
        'quadra': "  ",
        'full_house': "  ",
        'sequencia_baixa': "  ",
        'sequencia_alta': "  ",
        'cinco_iguais': "  "
    }
}

n_rolamentos = 0
funcoes.imprime_cartela(cartela_de_pontos)
dados_r = funcoes.rolar_dados(5)
dados_g = []
lista = ["1","2","3","4","5","6","sem_combinacao", "quadra", "full_house", "sequencia_baixa", "sequencia_alta", "cinco_iguais"]
lista_2 = []
i = 0
while i < 12:
    print("Dados rolados:", dados_r)
    print("Dados guardados:", dados_g)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acao = str(input())
    if acao == "0":
        print("Digite a combinação desejada:")
        combinacao = str(input())
        if combinacao in lista:
            if combinacao not in lista_2:
                lista_2.append(combinacao)
                contador = 0
                while contador < len(dados_r):
                    funcoes.guardar_dado(dados_r, dados_g, contador) 
                    contador = 0
                funcoes.faz_jogada(dados_g, combinacao, cartela_de_pontos)
                dados_r = funcoes.rolar_dados(5)
                dados_g = []
                n_rolamentos = 0
            else:
                print("Essa combinação já foi utilizada.")
        else:
            print("Combinação inválida. Tente novamente.")
        i += 1
    elif acao == "1":
        print("Digite o índice do dado a ser guardado (0 a 4):")
        dado_es = int(input())
        funcoes.guardar_dado(dados_r, dados_g, dado_es)
    elif acao == "2":
        print("Digite o índice do dado a ser removido (0 a 4):")
        dado_el = int(input())
        a = funcoes.remover_dado(dados_r, dados_g, dado_el)
        dados_r = a[0]
        dados_g = a[1]
    elif acao == "3":
        if n_rolamentos <= 1:
            dados_r = funcoes.rolar_dados(len(dados_r))
        else:
            print("Você já usou todas as rerrolagens.")
        n_rolamentos += 1
    elif acao == "4":
        funcoes.imprime_cartela(cartela_de_pontos)
    else:
        print("Opção inválida. Tente novamente.")
soma = 0
for valor in cartela_de_pontos["regra_simples"].values():
    soma += valor
pontuacao_rs = soma
soma = 0
for valor in cartela_de_pontos["regra_avancada"].values():
    soma += valor
pontuacao_ra = soma
if pontuacao_rs >= 63:
    pontuaca_final = pontuacao_rs + pontuacao_ra + 35
else:
    pontuaca_final = pontuacao_rs + pontuacao_ra


funcoes.imprime_cartela(cartela_de_pontos)
=======
import funcoes

cartela_de_pontos = {
    'regra_simples':  {
        1:"  ",
        2:"  ",
        3:"  ",
        4:"  ",
        5:"  ",
        6:"  "
    },
    'regra_avancada' : {
        'sem_combinacao':"  ",
        'quadra': "  ",
        'full_house': "  ",
        'sequencia_baixa': "  ",
        'sequencia_alta': "  ",
        'cinco_iguais': "  "
    }
}

n_rolamentos = 0
funcoes.imprime_cartela(cartela_de_pontos)
dados_r = funcoes.rolar_dados(5)
dados_g = []
lista = ["1","2","3","4","5","6","sem_combinacao", "quadra", "full_house", "sequencia_baixa", "sequencia_alta", "cinco_iguais"]
lista_2 = []
i = 0
while i < 12:
    print("Dados rolados:", dados_r)
    print("Dados guardados:", dados_g)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acao = str(input())
    if acao == "0":
        print("Digite a combinação desejada:")
        combinacao = str(input())
        if combinacao in lista:
            if combinacao not in lista_2:
                lista_2.append(combinacao)
                contador = 0
                while contador < len(dados_r):
                    funcoes.guardar_dado(dados_r, dados_g, contador) 
                    contador = 0
                funcoes.faz_jogada(dados_g, combinacao, cartela_de_pontos)
                dados_r = funcoes.rolar_dados(5)
                dados_g = []
                n_rolamentos = 0
            else:
                print("Essa combinação já foi utilizada.")
        else:
            print("Combinação inválida. Tente novamente.")
        i += 1
    elif acao == "1":
        print("Digite o índice do dado a ser guardado (0 a 4):")
        dado_es = int(input())
        funcoes.guardar_dado(dados_r, dados_g, dado_es)
    elif acao == "2":
        print("Digite o índice do dado a ser removido (0 a 4):")
        dado_el = int(input())
        a = funcoes.remover_dado(dados_r, dados_g, dado_el)
        dados_r = a[0]
        dados_g = a[1]
    elif acao == "3":
        if n_rolamentos <= 1:
            dados_r = funcoes.rolar_dados(len(dados_r))
        else:
            print("Você já usou todas as rerrolagens.")
        n_rolamentos += 1
    elif acao == "4":
        funcoes.imprime_cartela(cartela_de_pontos)
    else:
        print("Opção inválida. Tente novamente.")
soma = 0
for valor in cartela_de_pontos["regra_simples"].values():
    soma += valor
pontuacao_rs = soma
soma = 0
for valor in cartela_de_pontos["regra_avancada"].values():
    soma += valor
pontuacao_ra = soma
if pontuacao_rs >= 63:
    pontuaca_final = pontuacao_rs + pontuacao_ra + 35
else:
    pontuaca_final = pontuacao_rs + pontuacao_ra


funcoes.imprime_cartela(cartela_de_pontos)
>>>>>>> 3be0a2b9b2b05e2c48e9e67378c1724135ef05b2
print("Pontuação total:", pontuaca_final)