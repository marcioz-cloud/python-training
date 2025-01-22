casa = float(input("Qual valor da casa? "))
salario = float(input("Qual seu salario? "))
anos = float(input("Em quantos anos vai pagar? "))

v = 0.3*salario
p = (casa/anos)

if p >= v :
    print(f"Voce pode comprar essa casa, pois 30% do seu salario que eh R${v}, por sua vez eh menor ou igual a prestacao R${p:0.2f} ")
else:
    print(f"Voce nao pode comprar essa casa, pois 30% do seu salario que eh R${v}, por sua vez eh maior que a prestacao R${p:0.2f}")