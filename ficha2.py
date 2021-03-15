import math
area1 = [           "..*..",
                    ".*.*.",
                    "*...*",
                    ".*.*.",
                    "..*.."]
area2 = ["..*..",
                    ".*.*.",
                    "*....",
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
            #Criamos um visitados para saber os pontos que foram visitados
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


#Outputs parecem estar de acordo com a resoluçao do stor
print(area((3,2),area1))    #Output - 5

print(area((3,2),area2))    #Output - 12


'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''


artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
                       "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
                       "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
                      }

def erdos(artigos,n):
    #É nos dado logo de inicio o numErdos de Paul Erdos
    numErdos = {"Paul Erdos" : 0}
    #Utilizaremos uma queue para calcular o numErdos de cada coautor associados a um autor
    queue = ["Paul Erdos"] 
    while queue:
        #Tiramos o elemento da frente da queue para compararmos com os outros autores
        autor = queue.pop(0)
        #Percorremos os artigos todos
        for paper in artigos:
            #Percorremos os coautores de cada artigo de o autor estiver la
            if autor in artigos[paper]:
                
                for autor2 in artigos[paper]:
                    #Calculamos o numErdos de cada coautor e adicionamo-lo à queue
                    if autor2 not in numErdos:
                        #Como estamos a contruir de baixo para cima nao precisamos de verificar se exite um numErdos menor
                        numErdos[autor2] = numErdos[autor] + 1 
                        queue.append(autor2)
    #Queremos apenas os nomes          
    final = [x for x in numErdos if numErdos[x] <= n]
    #Sort por ordem alfabetica      -   Criterio secundario
    final.sort()
    #Sort pelo numErdos crescente   -   Criterio primario
    final.sort(key = lambda n: numErdos[n])
    #Retornamos a lista final
    return final



print(erdos(artigos,2))


