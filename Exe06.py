'''
6.Crie um programa que leia dois valores para as variáveis A e B,
que efetue a troca dos valores de forma que a variável A passe a ter o valor da variável 
B que a variável B passe a ter o valor da variável A. Apresente os valores trocados. 
Exemplo:
A=5
B=10
INVERTENDO
A=10
B=5
'''

X, Y = map(float, input("Fala 2 numeros: ").split())

print("X=", X, "Y=", Y)

print("Vou inverter os números: ")

X, Y = Y, X
print("X=", X, "Y=", Y)