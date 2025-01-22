distancia = int(input("Qual a distancia? "))

if distancia <= 200:
    custo = distancia*(0.5)
    print(f"custo da gasosa vai ser de {custo}")
else:
    c1 = distancia*(0.45)
    print(f"custo da gasosa vai ser de {c1}")
