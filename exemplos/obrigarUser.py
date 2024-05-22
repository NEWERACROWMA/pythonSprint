def Escolha(lista_opcoes, msg):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        escolha = input(msg)
    return escolha


lista = ['Chateau Le Pin', 'Jurupinga', 'Askov', 'Vodka']
opcoes = ['continuar', 'sair']

print('--------VINHOS--------')
print('')
print('1- CHATEAU LE PIN  | R$250,00')
print('')
print('2-    JURUPINGA    | R$150,00')
print('')
print('3-      ASKOV      | R$250,00')
print('')
print('4-      VODKA      | R$250,00')
print('')

opcao = Escolha('DIGA O VINHO QUE DESEJA COMPRAR: ')
cont_ou_nao = Escolha('VOCÊ DESEJA CONTINUAR OU NÃO?')