# main.py

from funcao_main import obter_dados_usuario, confirmar_dados, exibir_menu
import bet
import loja
import sobre

def main():
    nome, email, idade = obter_dados_usuario()
    if not confirmar_dados(nome, email, idade):
        nome, email, idade = obter_dados_usuario()
    
    while True:
        escolha = exibir_menu(idade)
        if escolha == 1:
            sobre.executar()
        elif escolha == 2 and idade >= 18:
            bet.executar()
        elif escolha == 3:
            loja.executar(nome, email, idade)
        elif escolha == 4:
            print('Obrigado por visitar o nosso site!')
            break

if __name__ == '__main__':
    main()
