""" pega um array ordenado e um item. se o item estiver na lista, retorna a posicao dele, se não, retorna None. dessa forma vc é capaz de saber em qual ponto da lista continuar procurando 
"""

def pesqisa_binaria(lista, item):
    # mantem o controle de que parte da lista vc esta procurando
    baixo = 0 # num a partir da posição inicial para o meio
    alto =len(lista) - 1 # num de elementos - o que quero achar
    
    # enquanto vc não reduziu a um elemento
    while baixo <= alto:
        # cheque o elemento do meio
        meio = (baixo + alto) // 2 # sera arredondado para baixo se não for par
        chute = lista[meio]
        
        # achou o item
        if chute == item:
            return meio
        # chute muito alto
        if chute > item:
            alto = meio - 1
        # chute muito baixo
        else:
            baixo = meio + 1
    
    # item não existe
    return None
