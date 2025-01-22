#Cores no terminal

nome = "marcio"

cores = {'amarelo': '\033[33m',
         'azul': '\033[34m',
         'limpo' : '\033[m',
         'vermelho' : '\033[31m'}
cor = input("Qual cor voce quer? ")

print(f"Ola! Muito prazer em te conhecer {cores[cor]}{nome}")