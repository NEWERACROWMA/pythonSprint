def executar():
    print('O Grupo Mahindra, fundado em 1945, é uma das maiores e mais admiradas federações multinacionais de empresas,'
          ' com 260.000 funcionários em mais de 100 países. Ele ocupa uma posição de liderança no setor de equipamentos agrícolas, '
          'veículos utilitários, tecnologia da informação e serviços financeiros na Índia e é a maior empresa de tratores do mundo em volume. '
          'Ele tem forte presença em energia renovável, agricultura, logística, hospitalidade e imobiliário. O Grupo Mahindra tem um foco claro em '
          'liderar globalmente o ESG (Environmental, Social, and Governance), capacitar a prosperidade rural e melhorar a vida urbana, com o objetivo de '
          'impulsionar mudanças positivas nas vidas de comunidades e stakeholders para que eles possam se elevarem.')
    while True:
        continuar = input('Deseja voltar para a página principal? (S/N) \n--->').upper()
        if continuar == 'S':
            return True
        elif continuar == 'N':
            print('Encerrando o programa. Obrigado por visitar a página Sobre.')
            return False
        else:
            print('Opção inválida. Por favor, digite S para sim ou N para não.')
