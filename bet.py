from funcao_BET import adicionar_aposta, exibir_resumo, perguntar_continuar, perguntar_corredores,perguntar_continuar_corredores, adicionar_aposta_corredor, apostar_corredor, exibir_resumo_corredores

print("Bem vindo à nossa aba de apostas da Formula-E!")

total_apostas = 0
apostas = {}

while True:
    total_apostas = adicionar_aposta(apostas, total_apostas)
    
    continuar = perguntar_continuar()
    if continuar != 's':
        break

exibir_resumo(apostas, total_apostas)
