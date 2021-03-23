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


'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''
vizinhos =  [["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
vizinhos2 = [["Portugal","Espanha"],["Espanha","França"]]
vizinhos3 = [["Portugal","Espanha"],["Canada","Estados Unidos"],["Estados Unidos","México"]]

def continente(fronteiras):
    #Essencial para a recursividade mais à frente
    #Verificamos se o input nao é vazio
    if fronteiras == []:
        return 0
    

    #Iniciamos o tamanho do continente e os visitados
    tamanhoContinente = 0
    visitados = []


    lista = fronteiras
    lista.sort(key= lambda a : len(a),reverse=True)

    #Em principio o maior continente tera o pais com mais fronteiras
    #Dai nos ordenarmos a lista pelo numero de fronteiras
    visitados = lista[0]
    tamanhoContinente = 0

    #Pegamos em todos os paises que obtivemos anteriormente e adicionamos os paises que fazem fronteira com estes

    for pais in lista[0]:
        for fronteira in lista[1:]:
            if pais in fronteira:
                for outro_pais in fronteira:
                    if outro_pais not in visitados:
                        visitados.append(outro_pais)

    #Verificamos se nao existem continentes com apenas pares de fronteiras que sejam maiores
    #Ex.: [["Portugal","Espanha"],["Canada","Estados Unidos"]["Estados Unidos","México"]]
    #Dado este input a funcao , sem o segmento de baixo, iria dar um output de 2, quando deveria dar 3
    tamanhoContinente = len(visitados)
    if continente(lista[1:]) > tamanhoContinente:
        tamanhoContinente = continente(lista[1:])
                

    return tamanhoContinente



    

  



print(continente(vizinhos))
print(continente(vizinhos2))
print(continente(vizinhos3))




'''
O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
'''

#o é um ponto, ou seja tem a forma o=(x,y)
def saltos(o,d):

    if o == d:
        return 0

    estrutura = [(o[0],o[1],0)]
    visitados = set()

    
    while(estrutura):
        x , y, nsaltos = estrutura.pop(0)
        visitados.add((x,y))
        

        for xMais in [-1,1]:
            for yMais in [-1,1]:
                if  (x + xMais,y + yMais * 2) == d or (x + xMais * 2,y + yMais) == d:
                    return nsaltos + 1
                if  (x + xMais,y + yMais * 2)   not in  visitados:
                    estrutura.append((x + xMais,y + yMais * 2,nsaltos + 1))
                if  (x + xMais * 2,y + yMais)   not in  visitados:
                    estrutura.append((x + xMais * 2,y + yMais,nsaltos+1))

    

print("Saltos")
print(saltos( (0,0) , (7,7) ))
rotas = [
                    ["Porto",20,"Lisboa"],
                    ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
                    ["Braga",3,"Famalicao",3,"Porto"],
                    ["Viana",4,"Povoa",3,"Porto"],
                    ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]
                    ]

# @carricosauro
def fixRotas(rotas):
    lista = []
    
    for rota in rotas:
        posOrigem = 0
        posDestino = 2
        posPreco = 1
        while posDestino + 1 <= len(rota):
            lista.append([rota[posOrigem],rota[posPreco],rota[posDestino]])
            posOrigem = posDestino
            posDestino += 2
            posPreco += 2
    
    return lista
print(fixRotas(rotas))


def viagem(rotas,o,d):
    rotas = fixRotas(rotas)

    caminhos = {o:0} # { destino:preco }
    orla = [(o,0)] # [ (destino, preco) ]
    
    for cid, preco in orla:
        proximos = filter(lambda x: cid in x, rotas)
        
        
        for prox in proximos:
            print(orla)
            print(proximos)
            if prox[0] == cid:
                proximoDestino = prox[2]
            else:
                proximoDestino = prox[0]
            novoPreco = preco + prox[1]
                
            if proximoDestino not in caminhos:
                caminhos[proximoDestino] = novoPreco
                orla.append((proximoDestino,novoPreco))
            elif novoPreco < caminhos[proximoDestino]:
                caminhos[proximoDestino] = novoPreco
                orla.append((proximoDestino,novoPreco))

    return caminhos[d]
                
print("Viagem")
print(viagem(rotas,"Braga","Caminha"))


mapalab = [         "  ########",
                    "# # #    #",
                    "# # #### #",
                    "# #      #",
                    "# # # ####",
                    "# # #    #",
                    "#   # #  #",
                    "##### ####",
                    "#        #",
                    "########  "]
def adjc(coord,n,mapa):
    orlacontent = []


   
        #Verificamos eixo do x
    if coord[0] < n-1 and mapa[coord[1]][coord[0]+1] == ' ' and (coord[2] == "" or coord[2][-1] != 'O'):
        orlacontent.append((coord[0]+1,coord[1],coord[2]+"E"))

    if coord[0] > 0 and mapa[coord[1]][coord[0]-1] == ' ' and (coord[2] == "" or coord[2][-1] != 'E'):
        orlacontent.append((coord[0]-1,coord[1],coord[2]+"O"))
        #Verificamos eixo do y
    if coord[1] < n-1  and mapa[coord[1]+1][coord[0]] == ' ' and (coord[2] == "" or coord[2][-1] != 'N'):
        orlacontent.append((coord[0],coord[1]+1,coord[2]+"S"))

    if coord[1] > 0 and mapa[coord[1]-1][coord[0]] == ' ' and (coord[2] == "" or coord[2][-1] != 'S'):
        orlacontent.append((coord[0],coord[1]-1,coord[2]+"N"))

    return orlacontent

#AKA labirinto
def caminho (mapa):
    #Vai guardar as posicoes e movimento feito para chegar la
    orla = [(0,0,"")]
    n=len(mapa)

    for coord in orla:
        if coord[0] == n-1 and coord [1] == n-1:
            return coord[2]
    
        orla += adjc(coord,n,mapa)
   



print(caminho(mapalab))





'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''

ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]


#Algoritmos de Floyd-Warshall que nos foi fornecido
def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist

#Vamos definir uma funçao que passe os os argumentos ao algoritmos de Floyd-Warshall
def buildRuas(ruas):
    adj= {}
    for rua in ruas:
        inicio  =   rua[0]
        fim     =   rua[-1]
        comprimento = len(rua)


        if inicio not in adj:
            adj[inicio] = {}

        if fim not in adj:
            adj[fim] = {}

        if fim not in adj[inicio]:
            adj[inicio][fim] = float("inf")


        if inicio not in adj[fim]:
            adj[fim][incio] =  float("inf")

        adj[inicio][fim] = min(comprimento,adj[inicio][fim])
        adj[fim][inicio] = min(comprimento,adj[fim][inicio])

    return adj

def tamanho (ruas):
    ruas = buildRuas(ruas)
    distancias = fw(ruas)

    tam = -1

    for dist in distancias:
        for n in distancias[dist]:
            m = distancias[dist][n]
            if m > tam:
                tam = m
    return tam

'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

def movsTravessia(mapa,y,x,lenMapa,widthMapa,custo,inicio):
    lista=[]

    for i in [-1,1]:
        #Eixo y
        if 0 <= y+i < lenMapa and y+i != 0:     #Garantimos que estamos dentro do mapa e que nao repetimmos coordenadas
            delta = abs(int(mapa[y][x]) - int(mapa[y+i][x]))
            if delta <= 2:
                lista.append((y+i,x,custo+delta+1,inicio)) 

        #Eixo x
        if 0 <= x+i < widthMapa and x+i != 0:   #Garantimos que estamos dentro do mapa e que nao repetimmos coordenadas
            delta = abs(int(mapa[y][x]) - int(mapa[y][x+i]))
            if delta <= 2:
                lista.append((y,x+i,custo+delta+1,inicio)) 

    return lista



def travessia(mapa):
    lenMapa = len(mapa)
    widthMapa = len(mapa[0])
    seen = {}
    #Orla terá a seguint forma orla=[y,x,custo,inicio] inicio será igual a x no inicio no entanto durante o inicio terá valor fixo e o x variará
    orla=[]
    for x in range(widthMapa):
        orla.append((0,x,0,x))
        seen[x] = set()
    menor=(0,float("inf"))


    for y, x , custo, inicio in orla:
        if (x,y) in seen[inicio]:
            continue
        seen[inicio].add((x,y))
        if y == lenMapa-1 and custo < menor[1]:
            menor = (inicio,custo)
        orla += movsTravessia(mapa, y , x , lenMapa, widthMapa , custo , inicio)


    return menor




