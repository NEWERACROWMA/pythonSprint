def obter_dados_usuario():
    nome = input('Diga seu nome: ')
    email = input('Diga seu E-mail: ')
    while True:
        idade_str = input('Diga sua idade: ')
        if idade_str.isnumeric():
            idade = int(idade_str)
            break
        else:
            print('Por favor, digite uma idade válida.')
    return nome, email, idade

def confirmar_dados(nome, email, idade):
    while True:
        confirma = input(f'Confirme suas informações: seu nome é {nome}, seu E-mail é {email} e sua idade é {idade}. Está certo? [S/N]: ').upper()
        if confirma == 'S':
            return True
        elif confirma == 'N':
            return False
        else:
            print('Resposta inválida. Por favor, digite S para sim ou N para não.')

def exibir_menu(idade):
    print('Escolha uma opção:')
    print('1. Sobre')
    print('2. BET')
    print('3. Loja')
    while True:
        escolha = input('Digite o número da opção desejada: ')
        if escolha.isnumeric():
            escolha = int(escolha)
            if escolha in [1, 2, 3]:
                if escolha == 2 and idade < 18:
                    print('Você não tem permissão para acessar a opção BET.')
                else:
                    return escolha
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
        else:
            print('Opção inválida. Por favor, digite um número.')

def main():
    nome, email, idade = obter_dados_usuario()
    print(f'Bem-vindo ao site, {nome}!')
    while not confirmar_dados(nome, email, idade):
        nome, email, idade = obter_dados_usuario()
    
    while True:
        escolha = exibir_menu(idade)
        if escolha == 1:
            print('Você escolheu Sobre o site.')
            break
        elif escolha == 2:
            print('Você escolheu BET.')
            break
        elif escolha == 3:
            print('Você escolheu Loja.')
            break

if __name__ == "__main__":
    main()
