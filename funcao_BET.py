from lista_BET import equipes, Mahindra_corredores, Jaguar_corredores, Maserati_corredores, Nissan_corredores

def Obter_resposta():
    while True:
        resposta = input(f"Em qual equipe você deseja apostar?\n{', '.join(equipes)}\n--> ")
        if resposta in equipes:
            return resposta
        else:
            print("Essa equipe não existe, escolha uma opção válida")

def Obter_times():
    while True:
        aposta = input("Quanto você deseja apostar?\n--> ")
        if aposta.isnumeric():
            return int(aposta)
        else:
            print("Você não digitou um valor válido, por favor digite apenas números")

def perguntar_corredores(equipe):
    while True:
        resposta = input(f"Deseja apostar nos corredores da equipe {equipe}? (s/n): ").lower()
        if resposta == 's':
            if equipe == 'Mahindra Racing':
                print("Corredores da equipe Mahindra:")
                for corredor in Mahindra_corredores:
                    print(corredor)
            elif equipe == 'Jaguar TCS Racing':
                print("Corredores da equipe Jaguar:")
                for corredor in Jaguar_corredores:
                    print(corredor)
            elif equipe == 'Maserati MSG Racing':
                print("Corredores da equipe Maserati:")
                for corredor in Maserati_corredores:
                    print(corredor)
            elif equipe == 'Nissan Formula E Team':
                print("Corredores da equipe Nissan:")
                for corredor in Nissan_corredores:
                    print(corredor)
            else:
                print("Equipe não encontrada.")
            break
        elif resposta == 'n':
            break
        else:
            print("Por favor, responda com 's' para sim ou 'n' para não.")

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

def adicionar_aposta(apostas, total_apostas):
    resposta = Obter_resposta()
    aposta_inicial = Obter_times()
    
    total_apostas += aposta_inicial

    if resposta in apostas:
        apostas[resposta] += aposta_inicial
    else:
        apostas[resposta] = aposta_inicial

    print(f"Você apostou na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")
    print(f"O seu total apostado até agora: R${total_apostas}")

    perguntar_corredores(resposta)
    
    return total_apostas

def adicionar_aposta_corredor(apostas_corredor, total_apostas_corredor, equipe):
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
        return apostas_corredor, total_apostas_corredor

    corredor, aposta_corredor = apostar_corredor(corredores)
    total_apostas_corredor += aposta_corredor

    if corredor in apostas_corredor:
        apostas_corredor[corredor] += aposta_corredor
    else:
        apostas_corredor[corredor] = aposta_corredor

    print(f"Você apostou no corredor {corredor} da equipe {equipe} e o valor apostado foi de R${aposta_corredor}.")
    print(f"O seu total apostado até agora nos corredores desta equipe: R${total_apostas_corredor}")

    return apostas_corredor, total_apostas_corredor

def exibir_resumo(apostas, total_apostas):
    print("Fim das apostas nas equipes. Obrigado por jogar!")
    
    if len(apostas) > 1:
        print(f"Você apostou em {len(apostas)} equipes.")
    else:
        print(f"Você apostou em 1 equipe.")

    for equipe, valor in apostas.items():
        print(f"Equipe: {equipe} - Valor apostado: R${valor}")

    print(f"O valor total apostado nas equipes foi de R${total_apostas}.")

def exibir_resumo_corredores(apostas_corredor, total_apostas_corredor):
    print("Fim das apostas nos corredores. Obrigado por jogar!")
    
    if len(apostas_corredor) > 1:
        print(f"Você apostou em {len(apostas_corredor)} corredores.")
    else:
        print(f"Você apostou em 1 corredor.")

    for corredor, valor in apostas_corredor.items():
        print(f"Corredor: {corredor} - Valor apostado: R${valor}")

    print(f"O valor total apostado nos corredores foi de R${total_apostas_corredor}.")

def perguntar_continuar():
    continuar = input("Deseja fazer outra aposta nas equipes? (s/n): ").lower()
    return continuar

def perguntar_continuar_corredores():
    continuar = input("Deseja fazer outra aposta nos corredores? (s/n): ").lower()
    return continuar

# Inicialização das variáveis
apostas = {}
total_apostas = 0

apostas_corredor = {}
total_apostas_corredor = 0

# Loop principal do programa para apostas nas equipes
while True:
    total_apostas = adicionar_aposta(apostas, total_apostas)
    
    continuar = perguntar_continuar()
    if continuar != 's':
        break

exibir_resumo(apostas, total_apostas)

# Loop principal do programa para apostas nos corredores
while True:
    equipe_corredores = Obter_resposta()
    total_apostas_corredor = adicionar_aposta_corredor(apostas_corredor, total_apostas_corredor, equipe_corredores)
    
    continuar = perguntar_continuar_corredores()
    if continuar != 's':
        break

exibir_resumo_corredores(apostas_corredor, total_apostas_corredor)