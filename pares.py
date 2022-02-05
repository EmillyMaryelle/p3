#Emilly Maryelle Xavier Pereira N519378

#Escreva uma função recursiva chamada pares(L) que retorna uma lista contendo apenas os números pares da lista L

#lista
list["x", "y"]

def pares(l,reserva): 
    if(l>reserva): 
        return
    print(l ,end=" ") 
    return pares(l+2,reserva) 
x=2
y=10
#verificando os numeros 
if(x % 2 ==0): 
    x=x 
else:      
    x+=1
pares(x,y)