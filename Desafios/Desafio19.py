#Desafio 19: Sorteie o nome de um aluno entre quatro opções.

# To import library random needed
import random

# To create the input of the students
a1 = input("student1: ")
a2 = input("student2: ")
a3 = input("student3: ")
a4 = input("student4: ")

# To create the list as object to be manipuled
list = (a1, a2, a3, a4)

# Function to create a random choice from the object list
esc = random.choice(list)

# Print result
print(esc)