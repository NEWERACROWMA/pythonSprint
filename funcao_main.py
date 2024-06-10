#Funções para operar a página principal, perguntando dados do usuário e o direcionando para a página que desejar
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
    print('4. Sair do site')
    while True:
        escolha = input('Digite o número da opção desejada: ')
        if escolha.isnumeric():
            escolha = int(escolha)
            if escolha in [1, 2, 3, 4]:
                if escolha == 2 and idade < 18:
                    print('Você não tem permissão para acessar a opção BET.')
                else:
                    return escolha
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
        else:
            print('Opção inválida. Por favor, digite um número.')
