def BuscaBin(lista, item:int) -> int:
    cursor_baixo = 0
    cursor_alto = len(lista) - 1
    
    while (cursor_baixo <= cursor_alto):
        meio = (cursor_baixo + cursor_alto)//2
        chute = lista[meio]
        
        if(chute == item):
            return meio
        if(chute > item):
            cursor_alto = meio - 1    
        else:
            cursor_baixo = meio + 1    
    return -1

######

def BuscaBinRecursiva():
    return -1


dados = [1, 2, 30, 41, 73, 81, 90, 101]

print(BuscaBin(dados, 81))
print(BuscaBin(dados, 103))