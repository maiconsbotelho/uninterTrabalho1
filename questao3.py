# BOAS VINDAS
print('\nBem-vindo a Fotocopiadora do Maicon da Silva Botelho RU: 1904125')


# FUNCAO PARA ESCOLHA DO SERVIÇO
def escolha_servico():
    while True:
        try:
            # MENU DE SERVIÇOS
            print('\nEntre com o tipo de serviço desejado')
            print('DIG - Digitalização')
            print('ICO - Impressão Colorida')
            print('IBO - Impressão Preto e Branco')
            print('FOT - Fotocópia')
            servico = input('>>').upper()

            # VERIFICA TIPO DE SERVIÇO ESCOLHIDO
            if servico not in ['DIG', 'ICO', 'IBO', 'FOT']:
                raise ValueError("Opção inválida. Escolha entre DIG, ICO, IBO ou FOT.")
            elif servico == 'DIG':
                return 1.10
            elif servico == 'ICO':
                return 1.00
            elif servico == 'IBO':
                return 0.40
            elif servico == 'FOT':
                return 0.20
            else:
                print('\n*** Escolha inválida ***\nPor favor tente novamente!')
        except ValueError as e:
            print('\n***', e, '***\nPor favor tente novamente!')


# FUNÇÃO PARA NÚMERO DE PÁGINAS
def num_pagina():
    while True:
        try:
            numeroPaginas = int(input('\nEntre com o número de páginas: '))

            # VERIFICA O NÚMERO DE PÁGINAS PARA APLICAR O DESCONTO
            if numeroPaginas < 0:
                raise ValueError("O número de páginas não pode ser negativo.")
            elif (numeroPaginas >= 20) and (numeroPaginas < 200):
                return numeroPaginas, 0.15
            elif (numeroPaginas >= 200) and (numeroPaginas < 2000):
                return numeroPaginas, 0.20
            elif (numeroPaginas >= 2000) and (numeroPaginas < 20000):
                return numeroPaginas, 0.25
            elif (numeroPaginas >= 20000):
                print(
                    '\n*** Não aceitamos tantas páginas de uma vez, valor máximo aceito é de 19999 páginas ***\nPor favor entre novamente com o número de páginas')
            else:
                return numeroPaginas, 0
        except ValueError as e:
            print('\n*** ', e, 'Apenas valores numéricos inteiros são aceitos ***\nPor favor tente novamente!')


# FUNÇÃO PARA ADICIONAR SERVIÇOS EXTRAS
def servico_extra():
    while True:
        try:
            # MENU DE SERVIÇOS EXTRAS
            print('\nDeseja adicionar mais algum serviço? ')
            print('1 - Encadernação Simples: R$ 15,00')
            print('2 - Encadernação Capa Dura: R$ 40,00')
            print('0 - Não desejo mais nada')
            extra = int(input('>> '))

            if extra not in [0, 1, 2]:
                raise ValueError("Opção inválida. Escolha entre 0, 1 ou 2.")
            elif extra == 1:
                return 15.00
            elif extra == 2:
                return 40.00
            elif extra == 0:
                return 0.00
            else:
                print('\n*** Opção inválida ***\nPor favor tente novamente!')
        except ValueError as e:
            print('\n***', e, '***\nPor favor tente novamente!')


# MAIN
servicoEscolhido = escolha_servico()
numeroPaginas, desconto = num_pagina()
servicoExtra = servico_extra()

# CALCULOS
valorSemDesconto = servicoEscolhido * numeroPaginas
valorComDesconto = valorSemDesconto - (valorSemDesconto * desconto)
valorTotal = valorComDesconto + servicoExtra

# FORMATAÇÃO DA PORCENTAGEM, EX.: DE 0.2% PARA 2%
descontoFormatado = desconto * 100

# IMPRESSÃO NO CONSOLE
print('================= Resumo do Pedido =================')
print('Custo por página: R$ {:.2f}'.format(servicoEscolhido))
print(
    '{} páginas: R$ {:.2f} - {:.0f}% (Desconto) = R$ {:.2f}'.format(numeroPaginas, valorSemDesconto, descontoFormatado,
                                                                    valorComDesconto))
print('Extras: R$ {:.2f}'.format(servicoExtra))
print('Valor total: R$ {:.2f}'.format(valorTotal))
print('=====================================================')
