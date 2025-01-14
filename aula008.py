# o Pyhthon ele vem leve sem todas as funcoes, modulos e bibliotecas para usar e programar
#por isso usamos o comando "import" para importar as bibliotecas especificas e suplementares

#para selecionar quais bibliotecas "from x import y" para economizar espaço

#ceil
#floor
#trunc
#pow
#sqrt
#factorial
#import math
#n = int(input("Digite o numero: "))
#r = math.sqrt(n)
#print(f"O numero da raiz de {n} eh igual a {math.ceil(r)} ")

#from math import sqrt,floor
#a =  int(input("qual numero? "))
#b = sqrt(a)
#(math.floor(b))

#import sys
#print(sys.version)

#DESAFIOS

#Desafio 16
#n = float(input("Numero real: "))
#i = n.__trunc__()
#print(f"O numero {n} tem a parte inteira {i}.")

#Desafio 17
import math
import random

#a = float(input("Qual cateto oposto: "))
#b = float(input("Qual cateto adjacente: "))
#h = math.hypot(a, b)
#print(f"A hipotenusa eh {h:.2f}")

#Desafio 18
#ang = float(input("Qual o angulo? "))
#sen = math.sin(math.radians(ang))
#cos = math.cos(math.radians(ang))
#tan = math.tan(math.radians(ang))
#print(f"Para o angulo de {ang:.2f} o seno eh {sen:.2f}, o cos eh {cos:.2f} e a tangente eh {tan:.2f}.")

#Desafio 19
#nom1 = input("Qual aluno 1? ")
#nom2 = input("Qual aluno 2? ")
#nom3 = input("Qual aluno 3? ")
#nom4 = input("Qual aluno 4? ")

#lista = [nom1, nom2, nom3, nom4]
#esc = random.choice(lista)
#print(esc)

#Desafio 20
import array
nom1 = input("Qual aluno 1? ")
nom2 = input("Qual aluno 2? ")
nom3 = input("Qual aluno 3? ")
nom4 = input("Qual aluno 4? ")

lista = [nom1, nom2, nom3, nom4]
#lista = (nom1, nom2, nom3, nom4)
#seq = 4

#sort = random.sample(lista, seq)

#random.shuffle()
#O que faz: Embaralha (altera a ordem) dos elementos de uma sequência in-place, ou seja,
# modifica diretamente a sequência original.
#Uso: É útil quando você deseja alterar a ordem dos elementos de uma lista e não precisa
# manter a sequência original.
#Não retorna nada; apenas modifica a lista original.

random.shuffle(lista)
print(lista)
#print("A sequencia eh: ")
#for i, numero in enumerate(sort, start=1):
    #print(f"{i}º número: {numero}")





#Desafio 21
