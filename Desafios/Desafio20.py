#Desafio 20: Embaralhe a ordem de uma lista de nomes.
#Dica: shuffle

#To import the library random
import random

#To create the input of student's name
a1 = input("Qual aluno1 ? ")
a2 = input("Qual aluno2 ? ")
a3 = input("Qual aluno3 ? ")
a4 = input("Qual aluno4 ? ")

#To create the list of names
lista = [a1, a2, a3, a4]
print(f"A ordem inicial era: {lista}")

#To shuffle the list randomly
random.shuffle(lista)

#To print the new list
print(f"A ordem de apresentacao sera: {lista}")