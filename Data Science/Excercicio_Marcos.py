# Exercício 3
# Dado a mesma tupla do exercício anterior, faça um programa que:
# O usuário visualiza o cardápio e digita qual item ele quer comprar.
# A seguir pergunta-se se ele quer algo a mais, caso ele queira, vai somando todos os valores do pedido numa variável soma.
# No final, printe para o usuário o valor total da conta dele
t1 = ('Doce', 'Bala ', 'Pizza ', 'Arroz ','Paçoca ', 'Pamonha')
t2 = ( 2.3, 0.15,  28.9, 4.5, 0.5, 5.4)
Final = 's'
print('-'*31)
print('-'*10,'Cardápio','-'*11,)
print('-'*31)
print('1 - ',t1[0],'............... : R$  ',t2[0])
print('2 - ',t1[1],'.............. : R$ ',t2[1])
print('3 - ',t1[2],'............. : R$ ',t2[2])
print('4 - ',t1[3],'............. : R$  ',t2[3])
print('5 - ',t1[4],'............ : R$  ',t2[4])
print('6 - ',t1[5],'............ : R$  ',t2[5])
print('-------------------------------')

soma = 0.0
i = 0
while True:
  i += 1
  num = int(input('Digite o seu pedido: '))
  print('-'*10, 'Cardápio', '-'*11,)
  print('-'*31)
  print('1 - ',t1[0],'............... : R$  ',t2[0])
  print('2 - ',t1[1],'.............. : R$ ',t2[1])
  print('3 - ',t1[2],'............. : R$ ',t2[2])
  print('4 - ',t1[3],'............. : R$  ',t2[3])
  print('5 - ',t1[4],'............ : R$  ',t2[4])
  print('6 - ',t1[5],'............ : R$  ',t2[5])
  print('-------------------------------')
  print('-'*31)
  soma = soma + t2[num-1]
  continua = input('você quer encerrar? (s/n) ')
  if continua == 's':
    break
print('-'*10, f'Total: R${soma:.2f}', '-'*11)