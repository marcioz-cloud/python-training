cidade = input("Em que cidade voce nasceu? ")

cidade.split()
x = cidade.find("Santo")

if x == 0:
    print("Cidade comeca com Santo")
else : print("Cidade nao comeca com Santo")