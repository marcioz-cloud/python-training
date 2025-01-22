#Alistamento

import time

#Verificacao de ano do candidato
ano = int(input("Qual seu ano de nascimento, candidato? "))

#Obtendo o ano atual baseado no OS
ano_atual = time.localtime().tm_year

#Calculo da idade
i = ano_atual-ano

#Calculando delay em anos
d = abs(i - 18)

#Controle condicional
if (i)== 18:
    print("Eh hora de se alistas")
elif (i)>= 18:
    print(f"Ja passou o tempo do alistamento ! Fazem {d} anos.")
else:
    print(f"Voce ainda vai se alistar, calma ! Faltam {d} anos") #Para garantir que um número inteiro seja sempre positivo em Python, você pode usar a função abs() do próprio Python, sem a necessidade de importar módulos adicionais.

