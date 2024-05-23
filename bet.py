equipes = ['Mahindra Racing', 'Jaguar TCS Racing', 'Maserati MSG Racing', 'Nissan Formula E Team']
Mahindra_corredores = ['Edoardo Mortara','Nick De Vries']
Jaguar_corredores = ['Mitch Evans','Nick Cassidy']
Maserati_corredores = ['Jehan Daruvala','Maximilian Gunther'] 
Nissan_corredores = ['Oliver Rowland','Sacha fenestraz']


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

total_apostas = 0

while True:
    resposta = obter_resposta()
    aposta_inicial = obter_aposta()
    
    total_apostas += aposta_inicial

    print(f"Você apostou na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")
    print(f"O seu total apostado até agora: R${total_apostas}")

    continuar = input("Deseja fazer outra aposta? (s/n): ").lower()
    if continuar != 's':
        break

print("Fim das apostas. Obrigado por jogar!")
resposta = obter_resposta()
aposta_inicial = obter_aposta()

print(f"Sua aposta foi na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")

