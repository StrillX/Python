"""

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""

produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]

def vendedor(capacidade, produtos):
    if capacidade == 0 or produtos == []:
        return 0,[]
    if capacidade < produtos[0][2]:
        return vendedor(capacidade, produtos[1:])
    
    cenario1 = vendedor(capacidade,produtos[1:])
    cenario2 = vendedor(capacidade-produtos[0][2],produtos)
    cenario3 = vendedor(capacidade-produtos[0][2],produtos[1:])
    cenario2 = cenario2[0] + produtos[0][1], cenario2[1] + [produtos[0][0]]
    cenario3 = cenario3[0] + produtos[0][1], cenario3[1] + [produtos[0][0]]



    resultado = (max(cenario3,cenario2,cenario1 ,key = lambda x : x[0]))
    
    resultado[1].sort()
    

    return resultado






print(vendedor(14,produtos))      # OUTPUT = (190,["biblia","biblia","microondas"]