# MENSAGEM DE BOAS VINDAS
print('\nBem-vindo a Loja de Gelados do Maicon da Silva Botelho RU: 1904125')

# APRESENTAÇÃO DO CARDÁPIO
print('---------------------Cardápio---------------------')
print('------| Tamanho | Cupuaçu (CP) | Açaí (AC) |------')
print('------|    P    |   R$  9,00   |  R$ 11,00 |------')
print('------|    M    |   R$ 14,00   |  R$ 16,00 |------')
print('------|    G    |   R$ 18,00   |  R$ 20,00 |------')
print('--------------------------------------------------')

# DECLARAÇÃO DE VARIÁVEIS
valor = 0

# INTERAÇÃO COM O CLIENTE
while True:
    sabor = input('\nEntre com o sabor desejado (CP/AC): ').lower()

    # VERIFICA SE O SABOR FOI ESCOLHIDO CORRETAMENTE
    if (sabor == 'ac' or sabor == 'cp'):
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').lower()

        # VERIFICA SE O TAMANHO FOI ESCOLHIDO CORRETAMENTE
        if (tamanho == 'p' or tamanho == 'm' or tamanho == 'g'):

            # AÇAÍ PEQUENO
            if (sabor == 'ac' and tamanho == 'p'):
                pedido = 11
                valor += pedido
                print('Você pediu AÇAÍ no tamanho P: R$ {:.2f}'.format(pedido))
                acrescentar = input('\nDeseja mais alguma coisa (Sim ou Nao)? ').lower()
                if (acrescentar == 'sim'):
                    continue

                else:
                    break


            # AÇAÍ MÉDIO
            elif (sabor == 'ac' and tamanho == 'm'):
                pedido = 16
                valor += pedido
                print('Você pediu AÇAÍ no tamanho M: R$ {:.2f}'.format(pedido))
                acrescentar = input('\nDeseja mais alguma coisa (Sim ou Nao)? ').lower()
                if (acrescentar == 'sim'):
                    continue

                else:
                    break

            # AÇAÍ GRANDE
            elif (sabor == 'ac' and tamanho == 'g'):
                pedido = 20
                valor += pedido
                print('Você pediu AÇAÍ no tamanho G: R$ {:.2f}'.format(pedido))
                acrescentar = input('\nDeseja mais alguma coisa (Sim ou Nao)? ').lower()
                if (acrescentar == 'sim'):
                    continue

                else:
                    break

            # CUPUAÇU PEQUENO
            elif (sabor == 'cp' and tamanho == 'p'):
                pedido = 9
                valor += pedido
                print('Você pediu CUPUAÇU no tamanho P: R$ {:.2f}'.format(pedido))
                acrescentar = input('\nDeseja mais alguma coisa (Sim ou Nao)? ').lower()
                if (acrescentar == 'sim'):
                    continue

                else:
                    break

            # CUPUAÇU MÉDIO
            elif (sabor == 'cp' and tamanho == 'm'):
                pedido = 14
                valor += pedido
                print('Você pediu CUPUAÇU no tamanho M: R$ {:.2f}'.format(pedido))
                acrescentar = input('\nDeseja mais alguma coisa (Sim ou Nao)? ').lower()
                if (acrescentar == 'sim'):
                    continue

                else:
                    break

            # CUPUAÇU GRANDE
            elif (sabor == 'cp' and tamanho == 'g'):
                pedido = 18
                valor += pedido
                print('Você pediu CUPUAÇU no tamanho G: R$ {:.2f}'.format(pedido))
                acrescentar = input('\nDeseja mais alguma coisa (Sim ou Nao)? ').lower()
                if (acrescentar == 'sim'):
                    continue

                else:
                    break

        else:
            print('Tamanho inválido. Tente novamente!')
    else:
        print('Sabor inválido. Tente novamente!')

# VALOR TOTAL DO PEDIDO
print('\nO valor total a ser pago: R$ {:.2f}'.format(valor))
