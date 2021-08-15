#converter str e arredondar para duas casas decimais
def roundF(arg):
    return round(float(arg), 2)


#gerador para usar com a saida do .children.values()
def gridIter(iterator, column=1):
    temp = iterator.copy()
    while 1:
        res = temp[:column]
        temp = temp[column:]

        if res: yield res
        else: break

