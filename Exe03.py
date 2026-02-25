'''
3. Desenvolva um programa para calcular e escrever a área e o perímetro de um retângulo.
Exemplo: 
Base= 5
Altura = 4
Área = 20
Perímetro = 18
'''

#Entrada
base = float(input('Informe a base do retangulo: '))
altura = float(input('Informe a altura do retangulo: '))

#Processamento 
area = base*altura
perimetro = (base*2)+(altura*2)

#saida
print('area do retangulo:', area) 
print('perimetro do retangulo:' ,perimetro)
