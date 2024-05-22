from funcoes import Escolha

listaProdutos = ['NFT1', 'NFT2', 'NFT3']
opcoes = ['continuar', 'sair']

print('Olá, bem vindo a nossa Loja Virtual!')
opc = Escolha(opcoes, 'Você deseja continuar ou voltar para a tela inicial? \n(continuar/sair) ->')

if opc == "sair":
    #AJUSTAR ISSO PARA VOLTAR PARA O MAIN
    print('voltar para o main.py')
else:
    print('Produtos disponíveis em nossa Loja:')
    for produto in listaProdutos:
        i = 0
        print(f'{i += 1} {produto}')
