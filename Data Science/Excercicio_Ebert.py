t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)
print('-'*30)
print('-'*10 + ' Cardapio ' + '-'*10)
print('-'*30)
passo = range(0,len(t1) - 2)
j = 0
for i in passo:
    print(f"{t1[j]:.<10} : R$ {t1[j+1]:.2f}")
    print('{0:.<10} : R$ {1:.2f}'.format(t1[j],t1[j+1]))
    j = j + 2
    if j > len(t1) - 2:
      break

print('-'*30)
soma = 0
while True:
  item = input('Informe o item desejado ')
  indItem = t1.index(item)
  soma += t1[indItem + 1]
  # soma = soma + t1[indItem + 1]
  if (input('deseja algo mais s/n? ')) == 'n':
    break
print('O valor total da sua compra é: {0:.2f}'.format(soma))