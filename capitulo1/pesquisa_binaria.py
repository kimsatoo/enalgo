
def pesqisa_binaria(lista, item):
    # mantem o controle de que parte da lista vc esta procurando
    baixo = 0
    alto =len(lista) - 1 
    
    # enquanto vc não reduziu a um elemento
    while baixo <= alto:
        # cheque o elemento do meio
        meio = (baixo + alto) // 2
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
    