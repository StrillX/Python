lista = [5,2,7,4,3,8]
lista2 = [15,27,14,38,26,55,46,65,85]


#           9% no codeboard


def crescente(lista):
    n = len(lista)
    lis = [1]*n


    for i in range(1,n):
        for j in range(0,i):
            if lista[i] > lista[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1
    
    maximum = 0
    print(lis)
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum

print(crescente(lista))
print(crescente(lista2))








