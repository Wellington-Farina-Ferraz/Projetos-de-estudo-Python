from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')
valor = Decimal('1254897.25')
print(locale.currency(valor, grouping=True))
# Prêmio da Mega-Sena
total = float( input('Premio total da Mega: ') )

# Número de ganhadores
num = int( input('Numero de ganhadores: ') )

print('O premio total foi R$%.2f para %d ganhadores, onde cada um ficou \
com R$%.2f' %(total,num,total/num))
