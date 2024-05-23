def Escolha(lista_opcoes, msg):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        escolha = input(msg)
    return escolha

#PAGINA DE BET

from listas import equipes, Mahindra_corredores, Jaguar_corredores, Maserati_corredores, Nissan_corredores

def obter_resposta():
    while True:
        resposta = input(f"Em qual equipe você deseja apostar?\n{', '.join(equipes)}\n--> ")
        if resposta in equipes:
            return resposta
        else:
            print("Essa equipe não existe, escolha uma opção válida")

def obter_aposta():
    while True:
        aposta = input("Quanto você deseja apostar?\n--> ")
        if aposta.isnumeric():
            return int(aposta)
        else:
            print("Você não digitou um valor válido, por favor digite apenas números")
