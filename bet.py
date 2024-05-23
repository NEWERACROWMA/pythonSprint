'''equipes = ['Mahindra Racing', 'Jaguar TCS Racing', 'Maserati MSG Racing', 'Nissan Formula E Team']


print("Bem vindo à nossa aba de apostas da Formula-E, nome")

while True:
    resposta = input(f"Em qual equipe você deseja apostar?\n-{equipes[0]}\n-{equipes[1]}\n-{equipes[2]}\n-{equipes[3]}\n--> ")
    if resposta not in equipes:
        print ("Essa equipe não existe, escolha uma opção válida")
    else:
        break

while True:
    aposta_inicial = input("Quanto você deseja apostar?\n--> ")
    if aposta_inicial.isnumeric():
        aposta_inicial = int(aposta_inicial)
        break
    else:
        print ("Você não digitou um valor válido, por favor digite apenas números")

print(f"Sua aposta foi na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.\nBoa sorte!!")

while True:
    apostar_dnv = input("Deseja apostar novamente?(Sim/Não)\n-->")
    if apostar_dnv == 'Sim':

'''
equipes = ['Mahindra Racing', 'Jaguar TCS Racing', 'Maserati MSG Racing', 'Nissan Formula E Team']

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

print("Bem vindo à nossa aba de apostas da Formula-E!")

resposta = obter_resposta()
aposta_inicial = obter_aposta()

print(f"Sua aposta foi na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")
