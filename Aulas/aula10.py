#Conditions - Simples e compostas / simplificada

n1 = int(input("Qual sua nota 1 ? "))
n2 = int(input("Qual sua nota 2 ? "))

m = (n1 + n2)/2

if m >= 6.0:
    print(f"Boas notas! Media {m}!")
else:
    print(f"Precisa estudar mais. Media {m}.")

print("-----FIM-----")