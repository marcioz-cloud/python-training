#Condições Aninhadas e Estruturas de repeticao

# if – Avalia uma condição e executa o bloco de código se a condição for verdadeira.
# elif (else if) – Avalia outra condição se a anterior for falsa.
# else – Define um bloco de código a ser executado caso todas as condições anteriores sejam falsas.

idade = 20

if idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")


# O for em Python é usado principalmente para percorrer elementos de uma sequência
# (listas, strings, tuplas, etc.) ou utilizar a função range() para iterar sobre um
# intervalo de números. Sintaxe básica:
for i in range(5):
    print(i)

#Exemplo com listas:
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
        print(fruta)

#Exemplo com range(start, stop, step):
for i in range(1, 10, 2):
        print(i)
    # Saída:
    # 1
    # 3
    # 5
    # 7
    # 9

# O while executa um bloco de código enquanto uma condição for verdadeira.
#Sintaxe básica:
contador = 0
while contador < 5:
        print(contador)
        contador += 1