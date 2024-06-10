from funcao_main import obter_dados_usuario, confirmar_dados, exibir_menu

def main():
    nome, email, idade = obter_dados_usuario()
    print(f'Bem-vindo ao site, {nome}!')
    while not confirmar_dados(nome, email, idade):
        nome, email, idade = obter_dados_usuario()

    continuar_executando = True
    while continuar_executando:
        escolha = exibir_menu(idade)
        if escolha == 1:
            print('Você escolheu o Sobre do site.')
            import sobre
            continuar_executando = sobre.executar()
        elif escolha == 2:
            print('Você escolheu BET.')
            import bet
            bet.executar()
        elif escolha == 3:
            print('Você escolheu Loja.')
            import loja
            continuar_executando = loja.executar()
        if not continuar_executando:
            print("Encerrando o programa. Obrigado por usar nosso site.")
            break

if __name__ == "__main__":
    main()
