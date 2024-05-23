from listas.lista_BET import equipes, Mahindra_corredores, Jaguar_corredores, Maserati_corredores, Nissan_corredores

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
    
    return total_apostas

def exibir_resumo(apostas, total_apostas):
    print("Fim das apostas. Obrigado por jogar!")
    
    if len(apostas) > 1:
        print(f"Você apostou em {len(apostas)} equipes.")
    else:
        print(f"Você apostou em 1 equipe.")

    for equipe, valor in apostas.items():
        print(f"Equipe: {equipe} - Valor apostado: R${valor}")

    print(f"O valor total apostado foi de R${total_apostas}.")

def perguntar_continuar():
    continuar = input("Deseja fazer outra aposta? (s/n): ").lower()
    return continuar == 's'