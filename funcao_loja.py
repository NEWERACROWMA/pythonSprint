# funcao_loja.py
#função para efetuar as compras dentro do sistema
def Escolha(opcoes, prompt):
    while True:
        escolha = input(prompt).strip().lower()
        if escolha in opcoes:
            return escolha
        else:
            print('Escolha inválida. Tente novamente.')
