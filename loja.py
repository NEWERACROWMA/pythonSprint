from funcoes import Escolha

listaProdutos = ['NFT1', 'NFT2', 'NFT3']
iden = ['1', '2', '3']

opcoes = ['continuar', 'sair']

print('Olá, bem vindo a nossa Loja Virtual!')
opc = Escolha(opcoes, 'Você deseja continuar ou voltar para a tela inicial? \n(continuar/sair) -> ')

if opc == "sair":
    #AJUSTAR ISSO PARA VOLTAR PARA O MAIN
    print('voltar para o main.py')
else:
    print('----- PRODUTOS -----\n')
    for i, produto in enumerate(listaProdutos, start=1):
        print(f'{iden[i-1]}. {produto}\n')
    opcNft = Escolha(iden,'Deseja visualizar algum dos NFTs?\n-> ')

