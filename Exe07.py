'''
7. Crie um programa que leia um valor de hora (hora:minutos) e informe (calcule) o total de minutos que se passaram 
desde o início do dia (0:00h).
Exemplo:
hora = 16
minuto = 45
minutos = 1005 
'''

tempo = input('Informe a hora e os minutos [12:34]')

horas = int(tempo[0:2])
minutos = int(tempo[3:6])
tempo_em_minutos = (horas*60) + minutos
print('Horas:', horas)
print('Minutos:', minutos)
print('Tempo decorrido em minutos:', tempo_em_minutos)