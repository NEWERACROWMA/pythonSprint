def Escolha(lista_opcoes, msg):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        escolha = input(msg)
    return escolha
