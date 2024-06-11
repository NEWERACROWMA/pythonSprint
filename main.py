# main.py

from funcao_main import obter_dados_usuario, confirmar_dados, exibir_menu
import bet
import loja
import sobre

def main():
    nome, email, idade = obter_dados_usuario()
    if not confirmar_dados(nome, email, idade):
        nome, email, idade = obter_dados_usuario()
#menu para direcionar o usuário para sua página de interesse
    while True:
        escolha = exibir_menu(idade)
        if escolha == 1:
            sobre.executar()
        elif escolha == 2:
            if idade >= 18:
                bet.executar(nome, email, idade)
            else:
                print("Desculpe, você precisa ter 18 anos ou mais para acessar esta seção.")
        elif escolha == 3:
            if idade >= 18:
                loja.executar(nome, email, idade)
            else:
                print("Desculpe, você precisa ter 18 anos ou mais para acessar esta seção.")
        elif escolha == 4:
            print('Obrigado por visitar o nosso site!')
            break
#garantir que a função seja executada apenas quando é executada diretamente
if __name__ == '__main__':
    main()
