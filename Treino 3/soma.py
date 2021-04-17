
"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""
lista = [-2,1,-3,4,-1,2,1,-5,4]




lista2 = [1,2,3,4,-11,1,2,3,4,5]



#Algoritmo de Kadane

#13% no codeboard

def maxsoma(lista):
    melhorsoma = float("-Inf")
    somaatual = 0
    for x in lista:
        somaatual = max(x, somaatual + x)
        melhorsoma = max (melhorsoma, somaatual)
    return melhorsoma


print(maxsoma(lista))
print(maxsoma(lista2))


