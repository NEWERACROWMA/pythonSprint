print("Bem vindo à nossa aba de apostas da Formula-E!")

from funcao_BET import adicionar_aposta, exibir_resumo, perguntar_continuar, adicionar_aposta_corredor, exibir_resumo_corredores, Obter_resposta, perguntar_continuar_corredores

# Inicialização das variáveis
total_apostas = 0
apostas = {}

total_apostas_corredor = 0
apostas_corredor = {}

# Loop principal do programa para apostas nas equipes
while True:
    total_apostas = adicionar_aposta(apostas, total_apostas)
    
    if not perguntar_continuar('equipes'):
        break

exibir_resumo(apostas, total_apostas)

# Loop principal do programa para apostas nos corredores
while True:
    equipe_corredores = Obter_resposta()
    apostas_corredor, total_apostas_corredor = adicionar_aposta_corredor(apostas_corredor, total_apostas_corredor, equipe_corredores)
    
    if not perguntar_continuar('corredores'):
        break

exibir_resumo_corredores(apostas_corredor, total_apostas_corredor)
