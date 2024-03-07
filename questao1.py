print('\nBem-vindo a Loja do Maicon da Silva Botelho RU: 1904125')

#ENTRADA DE DADOS
valorUnitario = float(input('Entre com o valor unitário do produto: R$ '))
quantidade = int(input('Entre com a quantidade do produto: '))

#CÁLCULO DO VALOR TOTAL SEM DESCONTO
valorTotal = valorUnitario * quantidade
print('O valor sem desconto foi R$ {:.2f}'.format(valorTotal))

#BASES PARA APLICAR DESCONTO
baseDesc1 = 2500
baseDesc2 = 6000
baseDesc3 = 10000

#PERCENTUAL DE DESCONTO DE ACORDO COM A BASE
desc1 = 4
desc2 = 7
desc3 = 11

#CONDIÇÕES PARA APLICAÇÃO DO DESCONTO CORRESPONDENTE

#ENTRE R$ 2500,00 E R$ 6000,00
if (valorTotal >= baseDesc1) and (valorTotal < baseDesc2):
    desconto = (valorTotal * desc1) / 100
    valorFinal = valorTotal - desconto
    print('O valor com desconto foi R$ {:.2f} (desconto de 4%)'.format(valorFinal))

#ENTRE R$ 6000,00 E R$ 10000,00
elif (valorTotal >= baseDesc2) and (valorTotal < baseDesc3):
    desconto = (valorTotal * desc2) / 100
    valorFinal = valorTotal - desconto
    print('O valor com desconto foi R$ {:.2f} (desconto de 7%)'.format(valorFinal))

#ACIMA DE R$ 10000,00
elif (valorTotal >= baseDesc3):
    desconto = (valorTotal * desc3) / 100
    valorFinal = valorTotal - desconto
    print('O valor com desconto foi R$ {:.2f} (desconto de 11%)'.format(valorFinal))

#ABAIXO DE R$ 2500,00
else:
    print('Valor total da compra R$ {:.2f}, (**Desconto apenas para compras acima de R$ 2500.00)'.format(valorTotal))