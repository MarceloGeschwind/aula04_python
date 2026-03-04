'''
8. Fazer um programa que dado um valor inteiro m calcule o menor número de notas de Real em que este número pode ser decomposto. Lembre-se que as notas existentes são 2, 5, 10, 20, 50 e 100. A Saída do programa deve ser o valor da entrada seguido de uma lista de notas correspondentes. 
Exemplo:
Valor R$ 1.451,00
R$ 100,00 -- 14 -- R$ 1.400,00
R$ 50,00 -- 0 -- R$ 0,00
R$ 20,00 -- 2 -- R$ 40,00
R$ 10,00 -- 0 -- R$ 0,00
R$ 5,00 -- 1 -- R$ 5,00
R$ 2,00 -- 3 -- R$ 6,00
Total: R$ 1.451,00
Qtd Notas: 20
'''

valor = int(input('valor do saque:'))
notas_100 = valor // 100
notas_50 = (valor % 100) // 50
notas_20 = ((valor % 100) % 50) // 20
notas_10 = (((valor % 100) % 50) % 20) // 10
notas_5 = ((((valor % 100) % 50) % 20) % 10) // 5
notas_2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
notas_1 = ((((((valor % 100) % 50) % 20) % 10) % 5) % 2) // 1

print('Valor: R$', valor)
print('R$ 100,00 --', '{:02}'.format(notas_100),'-- R${:8.2f}'.format(notas_100 * 100))
print('R$ 50,00 --',  '{:02}'.format(notas_50),'-- R${:8.2f}'.format(notas_50 * 50))
print('R$ 20,00 --',  '{:02}'.format(notas_20),'-- R${:8.2f}'.format(notas_20 * 20))
print('R$ 10,00 --',  '{:02}'.format(notas_10),'-- R${:8.2f}'.format(notas_10 * 10))
print('R$ 5,00 --',   '{:02}'.format(notas_5),'-- R${:8.2f}'.format(notas_5 * 5))
print('R$ 2,00 --',   '{:02}'.format(notas_2),'-- R${:8.2f}'.format(notas_2 * 2))
print('R$ 1,00 --',   '{:02}'.format(notas_1),'-- R${:8.2f}'.format(notas_1 * 1))