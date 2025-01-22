import random
import time

print("Vou pensar num numero entre 0 e 5. Tente adivinhar...")

n = input("Em que numero eu pensei ? ")
list = ('0', '1', '2', '3', '4', '5')
s = random.choice(list)

print("Processando")
time.sleep(2)

if n == s:
    print(f"Ganhei! Eu pensei no numero {s} e voce digitou {n}.")
else:
    print(f"Nao sabe, nao sabe... eu pensei no numero {s}.")