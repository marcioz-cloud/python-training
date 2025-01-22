#ano bissexto

ano = int(input("Qual seu ano? "))
b = ano%4

if b == 0 :
    print("Ano bissexto!")
else:
    print("Ano nao eh bissexto!")
    