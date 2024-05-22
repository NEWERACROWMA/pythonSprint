nome = input('Diga seu nome: ')
email = input('Diga seu E-mail: ')

while True:
    idade_str = input('Diga sua idade: ')
    if idade_str.isnumeric():
        idade = int(idade_str)
        break
    else:
        print('Por favor, digite uma idade válida.')

if idade < 18:
    print('Você não tem idade para entrar no site.')
else:
    print(f'Bem-vindo ao site, {nome}!')

    while True:
        confirma = input(f'Confirme suas informações: seu nome é {nome}, seu E-mail é {email} e sua idade é {idade}. Está certo? [S/N]: ').upper()
        if confirma == 'S':
            break
        else:
            nome = input('Diga seu nome: ')
            email = input('Diga seu E-mail: ')
            idade = 0
            while True:
                idade_str = input('Diga sua idade: ')
                if idade_str.isnumeric():
                    idade = int(idade_str)
                    break
                else:
                    print('Por favor, digite uma idade válida.')
            if idade < 18:
                print('Você não tem idade para entrar no site.')
                exit()

    print('Escolha uma opção:')
    print('1. Sobre')
    print('2. BET')
    print('3. Loja')

    while True:
        escolha = input('Digite o número da opção desejada: ')
        if escolha in ['1', '2', '3']:
            escolha = int(escolha)
            break
        else:
            print('Opção inválida. Por favor, digite um número entre 1 e 3.')

    if escolha == 1:
        print('Você escolheu Sobre o site.')
    elif escolha == 2:
        print('Você escolheu BET.')
    else:
        print('Você escolheu Loja.')