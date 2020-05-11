#Fatorial recursivo
def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1) 

print(fat(5))

#soma recursiva de valores de uma lista 
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

print(soma([2, 4, 8, 16, 32])) #62

#contar o numero de itens em uma lista

def count(lista):
    if lista == []:
        return 0
    return 1 + count(lista[1:])

print(count([2, 4, 8, 16, 32])) #5

#maior valor dentro de uma lista.
def maxValue(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    submax = maxValue(lista[1:])
    return lista[0] if lista[0] > submax else submax

print(maxValue([2, 4, 32, 8, 16])) 
        