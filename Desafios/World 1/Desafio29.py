velocidade = int(input("Qual a velocidade do carro? "))

if velocidade <= 80 :
    print("Voce esta indo bem")
else:
    multa = (velocidade - 80)*7
    print(f"Voce esta rapido demais, toma aqui uma multa de R${multa} reais")
