'''
1. Crie um programa que leia o salário de um funcionário e mostra na tela o seu salário anual.
Exemplo: 
salario_mensal = R$ 2000,00
salario_anual = R$ 24000,00
'''
print("Exercicio 01")

#Entrada
#Capturando o salario e covertendo para float
salario_mensal = float(input('Informe o salário mensal:'))

#PROCESSAMENTO
salario_anual = salario_mensal*12

#SAIDA
print('Salario anual: R$', salario_anual)
