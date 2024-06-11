# loja.py

from lista_loja import (
    listaProdutos, 
    prodEquipe, 
    prodVeiculo, 
    prodPiloto, 
    prodVelocidade, 
    prodCorrida, 
    prodPista, 
    prodVolta, 
    prodCodigo, 
    prodDesenho, 
    precoFinal,
    opcoes2
)
from funcao_loja import Escolha

def exibir_detalhes_completos(index):
    print(f'Equipe: {prodEquipe[index]}')
    print(f'Veículo: {prodVeiculo[index]}')
    print(f'Piloto: {prodPiloto[index]}')
    print(f'Velocidade: {prodVelocidade[index]}')
    print(f'Corrida: {prodCorrida[index]}')
    print(f'Pista: {prodPista[index]}')
    print(f'Tempo de Volta: {prodVolta[index]}')
    print(f'Código: {prodCodigo[index]}')
    print('-' * 40)

def exibir_preco_e_desenho(index):
    print(f'Preço Final: ${precoFinal[index]}')
    print(f'Desenho: {prodDesenho[index]}')
    print('-' * 40)

def executar(nome, email, idade):
    total_preco = 0
    produtos_comprados = []

    while True:
        print(f'Bem-vindo à loja, {nome}!')
        print('Selecione os produtos que deseja comprar:')
        produtos_disponiveis = False
        for i in range(len(listaProdutos)):
            if listaProdutos[i] not in produtos_comprados:
                print(f'{i + 1}. {listaProdutos[i]}')
                produtos_disponiveis = True

        if not produtos_disponiveis:
            print("Todos os produtos foram comprados.")
            break

        escolha = input('Digite o número do produto que deseja comprar (ou "sair" para finalizar a compra): ')

        if escolha.lower() == 'sair':
            break

        if not escolha.isnumeric() or int(escolha) < 1 or int(escolha) > len(listaProdutos):
            print('Escolha inválida. Tente novamente.')
            continue

        index = int(escolha) - 1

        if listaProdutos[index] in produtos_comprados:
            print('Este produto já foi comprado. Escolha outro produto.')
            continue

        exibir_preco_e_desenho(index)

        ver_detalhes = Escolha(opcoes2, 'Você deseja ver os detalhes completos deste produto? (sim/nao): ')
        if ver_detalhes == 'sim':
            exibir_detalhes_completos(index)

        confirmar = Escolha(opcoes2, 'Você deseja comprar este produto? (sim/nao): ')
        if confirmar == 'sim':
            total_preco += int(precoFinal[index].replace('$', ''))
            produtos_comprados.append(listaProdutos[index])
            print(f'Produto {listaProdutos[index]} adicionado ao carrinho.')
        
        print(f'Total atual: ${total_preco}\n')

    print(f'\nObrigado por comprar conosco, {nome}!')
    print('Produtos comprados:')
    for produto in produtos_comprados:
        print(f'- {produto}')
    print(f'Total a pagar: ${total_preco}')

    return total_preco
