nome = input("Digite seu nome completo: ")
print("Muito prazer em te conhecer!")

x = nome.split()

print(x)
v = len(x)

print(f"Seu primeiro nome eh {x[0]}")
print(f"Seu ultimo nome eh {x[v-1]}")