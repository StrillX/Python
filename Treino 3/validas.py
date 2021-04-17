"""

Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""
listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]


#   10% no codeboard

def validas(soma,listas):
    return list(filter(lambda x: somaExiste(soma,x),listas))

def somaExiste(soma,lista):




    for i in range(len(lista)):
        sum = lista[i]
        for j in range(i,len(lista)):
            if sum + lista[j] < soma:
                sum = sum + lista[j]
            elif sum + lista[j] > soma :
                j = j + 1
            else:
                return True

    return False


    

print(validas(10,listas))