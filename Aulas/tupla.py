#A principal forma de diferenciar uma tupla de uma lista em Python é pela sintaxe:
# Listas são definidas usando colchetes [ ], o que permite modificar os elementos.
# Tuplas são definidas usando parênteses ( ), o que torna os elementos imutáveis.
# Exemplo de lista (mutável):

minha_lista = [1, 2, 3, 4]
minha_lista.append(5)  # Adiciona um elemento na lista
print(minha_lista)  # [1, 2, 3, 4, 5]

#Exemplo de tupla (imutável):
minha_tupla = (1, 2, 3, 4)
# minha_tupla.append(5)  # Isso causaria erro, pois tuplas não suportam modificações
print(minha_tupla)  # (1, 2, 3, 4)

# Criando tuplas corretamente
# Tuplas podem ser criadas de diversas maneiras:

# Com parênteses (maneira padrão):
minha_tupla = (10, 20, 30)

# Sem parênteses (implícito): Python permite criar tuplas sem o uso explícito de parênteses, mas é uma prática menos comum.
minha_tupla = 10, 20, 30
print(type(minha_tupla))  # <class 'tuple'>


# Tupla de um único elemento (atenção com a vírgula): Para criar uma tupla com um único valor, é necessário colocar uma vírgula, pois sem ela Python não reconhece como tupla.
tupla_unitaria = (10,)  # Tupla válida
nao_tupla = (10)        # Isso é tratado como um inteiro, não como tupla

print(type(tupla_unitaria))  # <class 'tuple'>
print(type(nao_tupla))       # <class 'int'>

# Conversão de lista para tupla (usando a função tuple()):

lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # (1, 2, 3)