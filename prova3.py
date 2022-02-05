#Emilly Maryelle Xavier Pereira N 519378
lista1 = [55, 20]

def repete(e, n): 
    if n == 0:
        return []
    else:
        l = repete(e, n -1)
        l.append(e)
        return l
    
print(repete(55, "55")