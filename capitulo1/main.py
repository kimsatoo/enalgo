import pesquisa_binaria as pb

# l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

# para usar a PB em listas de strings, precisamos ordenar a lista
l = ["maria", "jonh", "ana", "pedro", "jose", "joao", "lucas", "jessica", "julia", "julio"]
# print(l)
l.sort()
# print(l)
item = pb.pesqisa_binaria(l, "jessica")
if item is not None:
    print("O item", l[item], "esta na posicao", item)
