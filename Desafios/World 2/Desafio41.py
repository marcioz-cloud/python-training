idade = int(input("Qual a sua idade? "))

if idade <= 9:
    print("Voce eh MIRIM.")
elif (14 > idade > 9):
    print("Voce eh INFATIL")
elif (19 > idade > 14):
    print("Voce eh JUNIOR")
elif (idade == 20):
    print("Voce eh SENIOR")
elif (idade > 20):
    print("Voce eh Master")