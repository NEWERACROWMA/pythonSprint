import os
from lista_BET import equipes, Mahindra_corredores, Jaguar_corredores, Maserati_corredores, Nissan_corredores
#
def Obter_resposta():
    while True:
        resposta = input(f"Em qual equipe você deseja apostar?\n{', '.join(equipes)}\n--> ")
        if resposta in equipes:
            return resposta
        else:
            print("Essa equipe não existe, escolha uma opção válida")
#
def Obter_times():
    while True:
        aposta = input("Quanto você deseja apostar?\n--> ")
        if aposta.isnumeric():
            return int(aposta)
        else:
            print("Você não digitou um valor válido, por favor digite apenas números")
#
def perguntar_corredores(equipe):
    while True:
        resposta = input(f"Deseja apostar nos corredores da equipe {equipe}? (s/n): ").lower()
        if resposta == 's':
            if equipe == 'Mahindra Racing':
                corredores = Mahindra_corredores
            elif equipe == 'Jaguar TCS Racing':
                corredores = Jaguar_corredores
            elif equipe == 'Maserati MSG Racing':
                corredores = Maserati_corredores
            elif equipe == 'Nissan Formula E Team':
                corredores = Nissan_corredores
            else:
                print("Equipe não encontrada.")
                return None
            return corredores
        elif resposta == 'n':
            return None
        else:
            print("Por favor, responda com 's' para sim ou 'n' para não.")
#
def apostar_corredor(corredores):
    while True:
        corredor = input(f"Em qual corredor você deseja apostar?\n{', '.join(corredores)}\n--> ")
        if corredor in corredores:
            while True:
                aposta = input("Quanto você deseja apostar neste corredor?\n--> ")
                if aposta.isdigit():
                    return corredor, int(aposta)
                else:
                    print("Por favor, insira um valor numérico válido.")
        else:
            print("Corredor não encontrado. Escolha uma opção válida.")
#
def adicionar_aposta(apostas, total_apostas):
    resposta = Obter_resposta()
    aposta_inicial = Obter_times()
    
    total_apostas += aposta_inicial

    if resposta in apostas:
        apostas[resposta]['total'] += aposta_inicial
    else:
        apostas[resposta] = {'total': aposta_inicial, 'corredores': {}}

    print(f"Você apostou na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")
    print(f"O seu total apostado até agora: R${total_apostas}")

    corredores = perguntar_corredores(resposta)
    if corredores:
        total_apostas = adicionar_aposta_corredor(apostas[resposta]['corredores'], corredores, total_apostas)

    return total_apostas
#
def adicionar_aposta_corredor(apostas_corredor, corredores, total_apostas):
    corredor, aposta_corredor = apostar_corredor(corredores)
    
    if corredor in apostas_corredor:
        apostas_corredor[corredor] += aposta_corredor
    else:
        apostas_corredor[corredor] = aposta_corredor

    print(f"Você apostou no corredor {corredor} e o valor apostado foi de R${aposta_corredor}.")
    total_apostas += aposta_corredor
    
    return total_apostas
#
def exibir_resumo(apostas, total_apostas):
    print("Fim das apostas. Obrigado por jogar!")
    
    for equipe, dados in apostas.items():
        print(f"Equipe: {equipe} - Valor apostado: R${dados['total']}")
        if dados['corredores']:
            for corredor, valor in dados['corredores'].items():
                print(f"  Corredor: {corredor} - Valor apostado: R${valor}")

    print(f"O valor total apostado foi de R${total_apostas}.")
#
def perguntar_continuar(tipo):
    while True:
        continuar = input(f"Deseja fazer outra aposta nas {tipo}? (s/n): ").lower()
        if continuar == 's':
            return True
        elif continuar == 'n':
            return False
        else:
            print("Por favor, responda com 's' para sim ou 'n' para não.")
