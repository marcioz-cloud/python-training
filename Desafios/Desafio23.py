n = input("Informe um numero: ")

print(f"Analisando o numero {n}...")

n.split()
c = len(n)

print(f"Unidade: {n[(c-1)]}")
print(f"Dezena: {n[(c-2)]}")
print(f"Centena: {n[(c-3)]}")
print(f"Milhar: {n[(c-4)]}")