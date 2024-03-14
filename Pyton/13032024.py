#se a è pari stampa b+c  se a è dispari stampo b-c
 
# per verificare se a è pari
#if a % 2 == 0:
# if a & 1 == 0:
#Math.floor(a/2)*2 == a:

"""
if a % 2 == 0:
    print(b + c)
else:
    print(b - c)

arit(10, 11, 12)
arit(11, 2 ,3)
arit(101, 1000, 2)
a, b, c=10, 20, 30
arit(b, c, a)
def Arit(a, b, c):
    if a % 2 == 0:
        print(b + c)
    else:
        print(b - c)
import random
list = ["rosso", "giallo", "verde", "blu", "arancio","ciano"]
def ColoreCasuale():
    return list[random.randint(0, len(list) -1)]
    
print (ColoreCasuale())



def Square(x)
    return x * x


def GeneraListaDigit():
    lista=[]
    for i in range(0, 10000):
        s=str(i)
        while len(s) < 4:
            s = "0"+s
        lista.append(s).
    return lista   
print(GeneraListaDigit())

def StringDigitsTolist():
    s=str(i)
    while len(s) < 4:
            s = "0"+s
    l1=[98123]
    for c in l1
        list(l1) 

            
        
    return lista   

print(StringDigitsTolist())
"""

#Modificare la GeneraListaDigit per generare una lista di liste del tipo
#[[0,0,0,0], [0,0,0,1], [0,0,0,2], ..., [9,9,9,8], [9,9,9,9]]
def GeneraListaDigit():
    lista=[]
    for i in range(0, 10000):
        s=str(i)
        while len(s) < 4:
            s = "0"+s
        lista.append(s)
    return lista   
print(GeneraListaDigit())

#zfill

def GeneraListaDigit():
    lista=[]
    for i in range(0, 10000):
        s = str(i)
        s = "0" * (4-len(s))+s
        #s=s.zfill(4)
        #while len(s) < 4:
        #   s = "0"+s
        lista.append(s)
    return lista   
print(GeneraListaDigit())
