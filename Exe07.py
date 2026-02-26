'''
7. Crie um programa que leia um valor de hora (hora:minutos) e informe (calcule) o total de minutos que se passaram 
desde o início do dia (0:00h).
Exemplo:
hora = 16
minuto = 45
minutos = 1005 
'''

hora, minuto = map(int, input("Fala alguma hora: ").split())
hora = (hora * 60)
print(hora + minuto)