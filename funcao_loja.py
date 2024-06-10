from lista_loja import opcoes2

def Escolha(lista_opcoes, msg):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        print('Escolha uma opção válida\n\n')
        escolha = input(msg)
    return escolha
