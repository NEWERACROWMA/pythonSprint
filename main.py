from funcao_main import obter_dados_usuario, confirmar_dados, exibir_menu

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