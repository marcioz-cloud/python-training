nome = str(input("Digite seu nome completo: "))

print("Analisando seu nome...")
print(f"Seu nome em maisuculas eh: {nome.upper()}")
print(f"Seu nome em minusculas eh: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - (nome.count(' '))} letras.")

x = nome.split() # aqui eu tenho uma lista com cada nome sendo um elemento

print(f"seu primeiro nome eh {x[0]} e ele tem {len(x[0])} letras") #fatiando a lista