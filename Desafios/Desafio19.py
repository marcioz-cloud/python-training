#Desafio 19: Sorteie o nome de um aluno entre quatro opções.
import random

a1 = input("student1: ")
a2 = input("student2: ")
a3 = input("student3: ")
a4 = input("student4: ")

list = (a1, a2, a3, a4)

esc = random.choice(list)
print(esc)