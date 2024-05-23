from funcoes import Obter_times, Obter_resposta

print("Bem vindo à nossa aba de apostas da Formula-E!")

total_apostas = 0

while True:
    resposta = Obter_resposta()
    aposta_inicial = Obter_times()
    
    total_apostas += aposta_inicial

    print(f"Você apostou na equipe {resposta} e o valor apostado foi de R${aposta_inicial}.")
    print(f"O seu total apostado até agora: R${total_apostas}")

    continuar = input("Deseja fazer outra aposta? (s/n): ").lower()
    if continuar == 'n':
        break

print("Fim das apostas. Obrigado por jogar!")
print(f"Sua aposta foi na equipe {resposta} e o valor apostado foi de R${total_apostas}.")
