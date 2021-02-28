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

    final = [nome for nome in nomes]
    final.sort(key = lambda final: final )
    final.sort(key = lambda final: len(final.split()) )
    
    return final
      
print(apelidos(nomes))



def factoriza(n):
    fatores_primos = []

    while n % 2 == 0:
        if 2 not in fatores_primos:
            fatores_primos.append(2)
        n = n / 2


    for i in range(3, int(math.sqrt(n) + 1),2):
        while n % i == 0:
            if i not in fatores_primos:
                fatores_primos.append(i)
            n = n / i

    if n > 2:
        fatores_primos.append(int(n))
    res = sum(fatores_primos)
    return res

print(factoriza(28))

texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
def frequencia(texto):
    string = texto.split()
    string.sort()
    
    cnt = Counter(string).most_common()
    
    final= [key for key,value in cnt]
        
    return final
    

print(frequencia(texto))



palavra = 'amanha'
def repete(palavra,n):
    final = ''
    while n > 0:
        final += palavra 
        n -= 1

    return final
print(repete(palavra,2))



prefs   = {10885:[1,5],40000:[5],10000:[1,2]}
prefs2  = {30000:[1],20000:[2],10000:[3]}


def aloca(prefs):
    sprefs={}

    sorted_keys = sorted(prefs.keys())
    used = []
    
    for i in sorted_keys:
        sprefs[i] = prefs[i]

    alocados = []

    for k in sprefs:
        for v in sprefs[k]:
            if v not in used:
                used.append(v)
                alocados.append(k)
                break
    todos   =   [key for key in sprefs]   
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
        for i in range(13):
            if i % 2 == 0:
                soma += int(livros[nome][i])
            else:
                soma += 3*(int(livros[nome][i]))
        if soma % 10 != 0 :
            invalidos.append(nome) 
            
    return sorted(invalidos)


print(isbn(livros))



log = [("****1234********","maria@mail.pt"),
                   ("0000************","ze@gmail.com"),
                   ("****1111****3333","ze@gmail.com")]



def hacker (log):
    dados = {}
    for num_cartao , email in log:
        if email not in dados:
            dados[email]= list(num_cartao)
        else:
            for i in range(16):
                if num_cartao[i] != '*' :
                    dados[email][i] = num_cartao[i]
    
    nconhecidos= {}
    for email in dados:
        nconhecidos[email] = 0
        for i in range(16):
            if dados[email][i] != '*':
                nconhecidos[email] += 1




    lista = [(k, v) for v,k in dados.items()]
    lista = [("".join(numeros),email) for numeros,email in lista]
  
    lista.sort(key = lambda t:  t[1])
 
    lista.sort(key = lambda t:  nconhecidos[t[1]], reverse = True)
   
    return lista
print(hacker(log))