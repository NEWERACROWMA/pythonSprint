from funcao_loja import Escolha

from desenho import colored_art1, colored_art2

from lista_loja import listaProdutos, iden, produto_dict, qtdProd, opcoes1, opcoes2, opcoes3, opcoes4

from lista_loja import prodCorrida, prodEquipe, prodPiloto, prodPista, prodVeiculo, prodVelocidade, prodVolta, prodCodigo, prodDesenho

from lista_loja import precoPiloto, precoBase, precoCircuito, precoCorrida, precoEquipe, precoFinal, precoPontos, precoTmpvolta, precoVeiculo



print('Olá, bem vindo a nossa Loja Virtual!')
opc = Escolha(opcoes1, 'Você deseja continuar ou voltar para a tela inicial? \n(continuar/sair) -> ')

while True:
    if opc == "sair":
        #AJUSTAR ISSO PARA VOLTAR PARA O MAIN
        print('voltar para o main.py')
    else:
        print('----- PRODUTOS -----\n')
        for i, produto in enumerate(listaProdutos, start=1):
            print(f'{i}. {produto}\n')
            i += 1
        opcNft = Escolha(iden,'Qual NFT você deseja visualizar?\nSelecione -> ')

        index = iden.index(opcNft) 

        while True:
            if opcNft in produto_dict:
                
                print("\n------------- REPRESENTAÇÃO ASCII -------------\n\n")
                print( prodDesenho[index])

                ver1 = Escolha(opcoes3, '1. Detalhes\n\n2. Código Criptografado Único\n\n3. Valores e Preço\n\n4. Voltar\n\n->')

                

                if ver1 == '1':
                    print("----- DETALHES DO NFT -----")
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

                    voltar = Escolha(opcoes2,'Você deseja voltar?\n(sim/nao)->')

                elif ver1 == '2':
                    print("CÓDIGO ÚNICO: ", '************************', "\n")
                    ver2 = Escolha(opcoes2, 'Você deseja visualizar o código do Produto NFT?: \n(sim) ->')
                    if ver2 == 'sim':
                        print("\n---------------- CÓDIGO ÚNICO ----------------\n\n",prodCodigo[index],"\n\nEste Produto é identificado como um 'Non-fungible token' (NFT), ele possui um ID único.\nEsses tokens são utilizados em sistemas digitais para representar propriedade única e indivisível de ativos digitais, como arte digital, colecionáveis, entre outros.\n\n")

                        voltar = Escolha(opcoes2,'Você deseja voltar?\n(sim)->')

                elif ver1 == '3':
                    print('O preço dos NFTs é baseado em contagem de pontos de acordo com suas estatísticas: \n\n')
                    print("\n------------- ACÚMULO DE PONTOS -------------\n\n")
                    print("Equipe: ", precoEquipe[index], "\n")
                    print("Veículo: ", precoVeiculo[index], "\n")
                    print("Piloto: ", precoPiloto[index], "\n")
                    print("Corrida: ", precoCorrida[index], "\n")
                    print("Circuito: ", precoCircuito[index], "\n")
                    print("Tempo de sua Melhor Volta: ", precoTmpvolta[index], "\n\n---------------------------------------------")
                    print("TOTAL DE PONTOS: ", precoPontos[index], "\n")
                    print("PREÇO BASE: ", precoBase[index], "\n")
                    print("----------------- PREÇO TOTAL -----------------\n\n", precoFinal[index], "\n")

                    ver3 = Escolha(opcoes4, 'O que deseja fazer?\n\n1. Adicionar ao carrinho\n\n2. Voltar')

                    if ver3 == '2':
                        voltar = Escolha(opcoes2,'Você deseja voltar?\n(sim)->')

            if ver1 == '4':
                voltar = Escolha(opcoes2,'Você deseja voltar?\n(sim)->')
                if voltar == 'sim':
                    break        
   
    


                
                    
