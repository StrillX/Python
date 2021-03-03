import math
from collections import Counter




nomes = [
            "Jose Carlos Bacelar Almeida",
            "Maria Joao Frade",
            "Jose Bernardo Barros",
            "Jorge Manuel Matos Sousa Pinto",
            "Manuel Alcino Pereira Cunha",
            "Xico Esperto"
]

        
    
def  apelidos(nomes):
    #Criamso uma list com todos os nomes
    final = [nome for nome in nomes]
    #Damos sort pelo criterio secundario -  Ordem Alfabetica
    final.sort(key = lambda final: final )
    #Damos sort pelo criterio primario -  Numero de nomes 
    final.sort(key = lambda final: len(final.split()) )
    
    return final
      
print(apelidos(nomes))



def factoriza(n):
    #Criamos um array para colocar cada fator que nao se repita 
    fatores_primos = []
    #Dividimos o numero por dois ate nao ser possivel
    while n % 2 == 0:
        if 2 not in fatores_primos:
            fatores_primos.append(2)
        n = n / 2

    #Verificamos todos os numeros ate a sqrt de n em procura de fatores primos
    for i in range(3, int(math.sqrt(n) + 1),2):
        while n % i == 0:
            if i not in fatores_primos:
                fatores_primos.append(i)
            n = n / i
    #Garantimos que o proprio numero nao é primo
    if n > 2:
        fatores_primos.append(int(n))
    #Somamos todos os fatores
    res = sum(fatores_primos)
    return res

print(factoriza(28))

texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
def frequencia(texto):
    #Dividimos o texto em palavras
    string = texto.split()
    #Ordenamos as palavras por ordem alfabetica
    string.sort()
    #Utilizamos um counter para contar as ocorrencias de cada palavra
    cnt = Counter(string).most_common()
    #apresentamos os dados da forma pedida
    final= [key for key,value in cnt]
        
    return final
    

print(frequencia(texto))



palavra = 'amanha'
def repete(palavra,n):
    #Contar o numero de letras no inicio da palavra que coincidem com as letras no final
    #Ex: aaabcaaa com um repete 2 ficaria aaabcaaabcaaa
    nrepetidos = 0
    indice=1
    for letra in range(len(palavra)//2):
        if palavra[letra] == palavra[-indice]:
            nrepetidos +=1;
        
        indice +=1
    print(nrepetidos)


    final = palavra
    n-=1
    
    while n > 0:
         
        n -= 1
        #apenas repetimos a partir do n repetidos, pois evitamos repeticoes de letras
        final += palavra[nrepetidos:]

    return final
print(repete(palavra,2))


prefs   = {10885:[1,5],40000:[5],10000:[1,2]}
prefs2  = {30000:[1],20000:[2],10000:[3]}


def aloca(prefs):
    sprefs={}
    #Damos sort pelo numero de aluno
    sorted_keys = sorted(prefs.keys())
    #Criamos um array com todos os trabalhos que tem um aluno associado
    used = []
    #Colocamos as preferencias num dicionario ordenado
    for i in sorted_keys:
        sprefs[i] = prefs[i]
    #Criamos uma list com os alunos que ficam alocados
    alocados = []
    #Percorremos os valores do dicionario ordenado
    for k in sprefs:
        for v in sprefs[k]:
            if v not in used:
                #Se o aluno quiser um trabalho disponivel esse trabalho passa a ocupado e o aluno fica com um trabalho atribuido
                used.append(v)
                alocados.append(k)
                break
    #pegamos numa lista com todos os alunos
    todos   =   [key for key in sprefs]   
    #E colocamos numa lista todos os alunos que nao tem um trabalho atribuido
    res     =   [x for x in todos if x not in alocados] 
    return res
    
      

print(aloca(prefs))
print(aloca(prefs2))

livros = {
                "Todos os nomes":"9789720047572",
                "Ensaio sobre a cegueira":"9789896604011",
                "Memorial do convento":"9789720046711",
                "Os cus de Judas":"9789722036757"
            }

def isbn (livros):
    
    invalidos  = []
    for nome in livros:
        soma = 0 
        #Verificaçao se o isbn é válido 
        for i in range(13):
            if i % 2 == 0:
                soma += int(livros[nome][i])
            else:
                soma += 3*(int(livros[nome][i]))
        #Se for invalido adicionamos à lista de invalidos
        if soma % 10 != 0 :
            invalidos.append(nome) 
    #Retornamos  a lista dos nomes ordenados 
    return sorted(invalidos)


print(isbn(livros))



log = [("****1234********","maria@mail.pt"),
                   ("0000************","ze@gmail.com"),
                   ("****1111****3333","ze@gmail.com")]



def hacker (log):
    #Criamos um dicionario para armazenar os numeros de cartao e emails
    dados = {}
    #Percorremos o log
    for num_cartao , email in log:
        #Se o email nao estiver no dicionario dados adicionamolo e guardamos o num_cartao associado
        if email not in dados:
            dados[email]= list(num_cartao)
        else:
        #Se o email ja esta no dados vamos comparar o num do cartao e vamos adicionar a nova informaçao ao numero
            for i in range(16):
                if num_cartao[i] != '*' :
                    dados[email][i] = num_cartao[i]
    # Aqui associamos os emails com o numero de numeros descobertos
    nconhecidos= {}
    for email in dados:
        nconhecidos[email] = 0
        for i in range(16):
            if dados[email][i] != '*':
                nconhecidos[email] += 1



    #Formatar a informaçao para a resposta
    lista = [(k, v) for v,k in dados.items()]
    lista = [("".join(numeros),email) for numeros,email in lista]
    #Criterio secundario de email por rodem alfabetica
    lista.sort(key = lambda t:  t[1])
    #Queremos ordenar por o n de digitos conhecidos como criterio primario
    lista.sort(key = lambda t:  nconhecidos[t[1]], reverse = True)
   
    return lista
print(hacker(log))

ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]

def cruzamentos(ruas):
    #Criamos um dicionario em que vamos colocar as keys como sendo 
    #o nome dos cruzamentos e os values como sendo o numero de ruas que vao ter a esse cruzamento
    ncruzamentos = {}
    for cruzamento in ruas:
        #Inserimos o primeiro cruzamento de ele nao estiver no ncruzamentos
        if cruzamento[0] not in ncruzamentos:
            ncruzamentos[cruzamento[0]] = 1
        #Caso ja exista somamos uma ocorrencia
        else:
            ncruzamentos[cruzamento[0]] += 1
        #Adicionamos o segundo cruzamento
        if cruzamento[-1] not in ncruzamentos:
            ncruzamentos[cruzamento[-1]] = 1
        #Garantimos que o cruzamento nao começa e acaba em si proprio
        elif cruzamento[0] != cruzamento[-1]:
            ncruzamentos[cruzamento[-1]] += 1
    #Tornamos a informaçao de um dicionario para uma lista de tuplos
    tuplofinal = list(ncruzamentos.items())
    #Como o criterio da ordem alfabetica é apenas de desempate utilizamos esse primeiro
    tuplofinal.sort(key = lambda t : t[0])
    #Agora damos sort pelo numero de cruzamentos
    tuplofinal.sort(key = lambda t : t[1])
    return tuplofinal
print(cruzamentos(ruas))

jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]

def tabela (jogos):
    #Criamos uma classificacao
    classificacao = {}
    for equipa1, golos1, equipa2,golos2 in jogos:
        #Percorremos os jogos que nos sao dados
        
        #Adicionamos a equipa caso ela nao esteja na classificacao
        if equipa1 not in classificacao:
            #Vamos ter duas informacoes para cada equipa, o numero de pontos e a diferença de golos
            classificacao[equipa1] = [0,0]
        if equipa2 not in classificacao:
            #Vamos ter duas informacoes para cada equipa, o numero de pontos e a diferença de golos
            classificacao[equipa2] = [0,0]

        #Damos update nas classificacoes
        #Calculamos quem ganha e a diferença de golos
        resultado = golos1-golos2

        if resultado > 0 :
            classificacao[equipa1][0] += 3
        elif resultado < 0:
            classificacao[equipa2][0] += 3
        else:
            classificacao[equipa1][0] += 1
            classificacao[equipa2][0] += 1
        #Aqui adicionamos a diferença de golos
        classificacao[equipa1][1] = resultado
        classificacao[equipa2][1] = -resultado
        #Formatamos a informacao
    classificacao_final = list(classificacao.items())
    #Sort pelo criterio terciario - NOME
    classificacao_final.sort(key= lambda t: t[0])
    #Sort pelo criterio secundario - Dif de golos - Descendente
    classificacao_final.sort(key= lambda t: t[1][1], reverse=True)
    #Sort pelo criterio primario - Numero de pontos - Descendente
    classificacao_final.sort(key= lambda t: t[1][0], reverse=True)

    
    classificacao_final = [(x,y[0]) for x, y in classificacao_final]
    
    return classificacao_final
print (tabela(jogos))



comandos = "EEAADAAAAAADAAAADDDAAAHAAAH"
def robot (comandos):
    #Lista onde aparecerao os vertices do retangulo
    lista_final=[]
    #Coordenandas do retangulo
    retangulo = [0,0,0,0]
    #Utilizamos uma variavel para sabermos a rotaçao do robot
    rotaçao = 0
    #Variaveis para calcular as posicoes
    x = y = 0
    for instruçao in comandos:
        #Roda para a esquerda
        if instruçao == "E":
            rotaçao -= 1
        #Roda para a direita
        elif instruçao == "D":
            rotaçao += 1
        #Avança
        elif instruçao == "A":
            #Virado para cima - y positivo
            if rotaçao % 4 == 0:
                y += 1
                retangulo[3] = max(y,retangulo[3])
            #Virado para a direita - x positivo
            if rotaçao % 4 == 1:
                x += 1
                retangulo[2] = max(x,retangulo[2])
            #Virado para baixo - y negativo
            if rotaçao % 4 == 2:
                y -= 1
                retangulo[1] = min(y,retangulo[1])
            #Virado para a esquerda - x negativo
            if rotaçao % 4 == 3:
                x -= 1
                retangulo[0] = min(x,retangulo[0])
        #Guarda posicao
        elif instruçao == "H":
            #Adicionamos o retangulo à lista
            lista_final.append(tuple(retangulo))
            #Reset no robot
            rotaçao = 0
            x = y = 0
            retangulo=[0,0,0,0]

            
    return lista_final
print(robot(comandos))

