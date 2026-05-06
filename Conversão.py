n = float(input('quanto dinheiro em reais você tem em sua carteira?: R$'))
valor = input('digite no que você quer converter:')
s = (n / 5)
s1 = (n * 0.17)
s2 = (n * 31.61)
s3 = (n * 185.74)
s4 = (n * 0.16)
if valor == 'dólares':
    print('com R${:.2f} reais você pode comprar cerca de US${:.2f} dólares'.format(n,s))
elif valor == 'euros':
    print('com R${:.2f} reais você pode comprar cerca de EUR${:.2f} euros'.format(n,s1))
elif valor == 'ienes':
    print('com R${:.2f} reais você pode comprar cerca de JPY¥{:.2f} ienes'.format(n,s2))
elif valor == 'kwanzas':
    print('com R${:.2f} reais você pode comprar cerca de Kz{:.2f} kwanzas'.format(n,s3))
elif valor == 'franco suíço':
    print('com R${:.2f} reais você pode comprar cerca de Fr{:.2f} franco suíço'.format(n,s4))
