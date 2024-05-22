equipe1 = 'Mahindra Racing'
equipe2 = 'Jaguar TCS Racing'
equipe3 = 'Maserati MSG Racing'
equipe4 = 'Nissan Formula E Team'

print("Bem vindo à nossa aba de apostas da Formula-E, nome")

while True:
    resposta = input(f"Em qual equipe você deseja apostar?\n{equipe1}\n{equipe2}\n{equipe3}\n{equipe4}\n--> ")
    if resposta not in (equipe1, equipe2, equipe3, equipe4):
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

print(f"Sua aposta foi na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")
