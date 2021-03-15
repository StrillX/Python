import math
area1 = [           "..*..",
                    ".*.*.",
                    "*...*",
                    ".*.*.",
                    "..*.."]

'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def area(ponto, mapa):
        #Garantimos que nao começamos numa posicao invalida
        if mapa[ponto[1]][ponto[0]] != '*':
            queue = [ponto]
            visitados = set()
        #Criamos uma queue para guardar os proximas posicoes a verificar
        while queue:
            x, y = queue.pop(0)
            visitados.add((x,y))

            adjacencia(x, y, mapa, visitados, queue)


        return len(visitados)
#Possivel alteracao para a utilizacao na funcao labirinto - alterar o caracter a comparar
def adjacencia(x, y, mapa, visitados, queue):
    for i in [-1,1]:
        #Verificamos se as coordenadas com y igual e adjacentes sao validas
        if 0 <= x+i < len(mapa) and (x + i , y) not in visitados and mapa[y][x + i] == '.':
            queue.append((x + i , y))
        #Verificamos o mesmo para as coordenadas com x igual
        if 0 <= y+i < len(mapa) and (x , y + i) not in visitados and mapa[y + i][x] == '.':
            queue.append((x , y + i))
    return queue

print(area((3,2),area1))