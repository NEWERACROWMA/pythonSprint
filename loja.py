from funcoes import Escolha
from listas import listaProdutos, iden, produto_dict, opcoes



print('Olá, bem vindo a nossa Loja Virtual!')
opc = Escolha(opcoes, 'Você deseja continuar ou voltar para a tela inicial? \n(continuar/sair) -> ')

if opc == "sair":
    #AJUSTAR ISSO PARA VOLTAR PARA O MAIN
    print('voltar para o main.py')
else:
    print('----- PRODUTOS -----\n')
    for i, produto in enumerate(listaProdutos, start=1):
        print(f'{i}. {produto}\n')
        i += 1
    opcNft = Escolha(iden,'Deseja visualizar algum dos NFTs?\nSelecione -> ')

    if opcNft in produto_dict:
        print(f'{opcNft}. {produto_dict[opcNft]}')
    else:
        print('Produto não listado')

