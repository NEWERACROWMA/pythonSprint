from funcoes import Escolha
from listas import listaProdutos, iden, produto_dict, qtdProd, opcoes
from listas import prodCorrida, prodEquipe, prodPiloto, prodPista, prodVeiculo, prodVelocidade, prodVolta

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
    opcNft = Escolha(iden,'Qual NFT você deseja visualizar?\nSelecione -> ')

    if opcNft in produto_dict:
        index = iden.index(opcNft)  # Obtém o índice do NFT selecionado
        print("----- INFORMAÇÕES DO NFT -----")
        print("NFT:", listaProdutos[index], "\n")
        print("ID:", iden[index], "\n")
        print("Quantidade:", qtdProd[index], "\n")
        print("Equipe:", prodEquipe[index], "\n")
        print("Veículo:", prodVeiculo[index], "\n")
        print("Piloto:", prodPiloto[index], "\n")
        print("Velocidade:", prodVelocidade[index], "\n")
        print("Corrida:", prodCorrida[index], "\n")
        print("Pista:", prodPista[index], "\n")
        print("Volta mais rápida:", prodVolta[index], "\n")
    else:
        print('Produto não listado')
