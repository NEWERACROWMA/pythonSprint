from funcao_BET import adicionar_aposta, exibir_resumo, perguntar_continuar

print("Bem-vindo à nossa aba de apostas da Formula-E!")

aposta_corredor = 0
total_apostas = 0
apostas = {}

while True:
    total_apostas = adicionar_aposta(apostas, total_apostas)
    
    if not perguntar_continuar('equipes'):
        break

exibir_resumo(apostas, total_apostas)
