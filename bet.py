from funcao_BET import adicionar_aposta, exibir_resumo, perguntar_continuar
from lista_BET import equipes, Mahindra_corredores, Jaguar_corredores, Maserati_corredores, Nissan_corredores

print("Bem vindo à nossa aba de apostas da Formula-E!")



# Inicialização das variáveis
total_apostas = 0
apostas = {}

# Loop principal do programa para apostas nas equipes e corredores
while True:
    total_apostas = adicionar_aposta(apostas, total_apostas)
    
    if not perguntar_continuar('equipes'):
        break

exibir_resumo(apostas, total_apostas)
