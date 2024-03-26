#Genera una lista che contiene N digit casuali tra 1 e N
import random         # random()

N=int(input("Scrivi un numero:"))
def GeneraLista(N):
    ls=[]
    for i in range(N):
        ls.append(random.randint(1,N))
    return ls
#print(GeneraLista(N))

def Contauguali (ls, lsCheck):
    totale=0
    ls=ls.copy()
    lsCheck=lsCheck.copy()
    for i in range(len(ls)):
        if ls[i] == lsCheck [i]:
            totale= totale + 1
    return totale
#print("Numeri uguali:", Contauguali ( GeneraLista(N), GeneraLista(N)))


#print("Numeri:", Contauguali ( GeneraLista(N), GeneraLista(N)))



def ContaUgualiInAltroPostoestesso (ls, lsCheck):
    ls=ls.copy()
    lsCheck=lsCheck.copy()
    stessoposto=0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            stessoposto += 1
            ls[i]=None
            lsCheck[i]=None
    altroposto=0    
    for i in range(len(lsCheck)):
        if lsCheck[i] != None and lsCheck[i] in ls:
            altroposto += 1
            ls.remove(lsCheck[i])
    return stessoposto, altroposto
#print(ContaUgualiInAltroPostoestesso(GeneraLista(N), GeneraLista(N)))

lists=(GeneraLista(N))
lists2=(GeneraLista(N))
print(Contauguali(lists,lists2))




