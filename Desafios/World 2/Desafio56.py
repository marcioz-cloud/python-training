nome1 = input("Qual seu nome1? ")
nome2 = input("Qual seu nome2? ")
nome3 = input("Qual seu nome3? ")
nome4 = input("Qual seu nome4? ")

idade1 = int(input(f"Qual sua idade {nome1}? "))
idade2 = int(input(f"Qual seu idade {nome2}? "))
idade3 = int(input(f"Qual seu idade {nome3}? "))
idade4 = int(input(f"Qual seu idade {nome4}? "))

sexo1 = input(f"Qual seu sexo {nome1}? ").lower()
sexo2 = input(f"Qual seu sexo {nome2}? ").lower()
sexo3 = input(f"Qual seu sexo {nome3}? ").lower()
sexo4 = input(f"Qual seu sexo {nome4}? ").lower()

m = ((idade1 + idade2 + idade3 + idade4)/4)

count_mulheres = 0
if idade1 <= 20 and sexo1 == "feminino":
    count_mulheres += 1

if idade2 <= 20 and sexo2 == "feminino":
    count_mulheres += 1

if idade3 <= 20 and sexo3 == "feminino":
    count_mulheres += 1

if idade4 <= 20 and sexo4 == "feminino":
    count_mulheres += 1

print(f"A media do grupo eh de {m} anos")
print(f"quantidade de mulheres com menos de 20 anos eh de {count_mulheres} mulheres")