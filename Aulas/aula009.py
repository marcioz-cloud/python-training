#fatiamento de string

frase = "Ola time"

#print(frase[5:9:2]) #excluindo o ultimo num do range : em grupos de 2
#print(frase[:6]) # do inicio da cadeia de string ate o caracter 6

#Analise de String
# print(len(frase)) #comprimento
# print(frase.count('a', 0, 8)) # quantidade de letras no range start/end
# print(frase.find('la')) #localizacao de inicio

# print('tim' in frase)
# print(frase.find('tim')) #verificar string dentro da string
# print(frase.replace('tim','tre')) #substituir texto

# print(frase.upper())
# print(frase.lower())
# title() -> letra de cada palavra maiuscula.
#capitalize() -> a primeira letra da string maiuscula

# frase.split()
# '-'.join(frase)
# print(frase)
#print(frase[::2])

# print("""
# Comentar/Descomentar Linhas Selecionadas
# Passo 1: Selecione as linhas de código que deseja comentar.
# Passo 2: Pressione o atalho de teclado:
# No Windows/Linux: Ctrl + /
# """) # Tres aspas duplas pode fazer print em varias linhas mas junto

new = frase.split()
print(new)