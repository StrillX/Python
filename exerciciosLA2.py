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


def funteste(x):
    return x

    


