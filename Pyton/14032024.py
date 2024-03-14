#Problema ho la stinga "123", la voglio strasformare in  [1,2,3]
#definire una funzione
"""
def lista():
    s="123"
    n=list(s)
    return(n)
print(lista())
"""
"""
def Converti(s):
    l=list(s)
    l1=[]
    for i in l:
        l1.append(int(i))
    return l1
print(converti("123"))
#oppure

def Converti(s):
    return[int(i) for i in s]
print(Converti("123"))
"""
"""
fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
#readlines legge tutte le linee incluso le linee a capo (eol/eoln)
#come tolgo i fine riga?
l1=[]
for l in linee:
    l1.append(l.strip()) #elimina spazi
linee=l1
print(linee)


s="alfa;beta;gamma"
#come posso ottenere la lista ["alfa", "beta", "gamma"]
print(s.split(";"))
"""
#dato alice stampare una per riga , tutte le parole che la compongono
fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
l1=[]
for l in linee:
    l1.extend(l.strip().split(" "))
    
 
linee=l1

"""

def maiuscolo(c):
    return c.isupper()
    return n % 2 == 0 #pari
print(list(filter(pari, lista#nome)))
"""

#data una lista di stringe , eliminare dalla lista tutte le stringe vuote
#ls=["uno", "", "due", "tre", "", "", "", "","fine"]
#    def SenzaVuto():
 #   vuota=[]
   #     for vuota in linee:
    #        if len(vuota) > 0:
     #           vuota.append(i)
        




fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
l1=[]
for l in linee:
    l1.extend(l.strip().split(" "))
linee=l1
print(linee)


#contare quanti caratteri ci sono in alice
#contare quanti caratteri non spazi bianchi ci sono in alice
#contare quanti caratteri alfanumerici[a-za-z0-9] ci sono in alice
fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
caratteri=0
for linea in linee:
    caratteri +=len(linea)
print("caratteri:", len(alice))




fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
notblank = 0
for c in alice:
    if c != " ":
        notblank += 1
#caratteri=0
#for linea in linee:
#    caratteri +=len(linea)
print("caratteri:", len(alice))
print("caratteribbb:", notblank)



fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
alfnum = 0
for c in alice:
    if c.isalnum():
        alfnum += 1
#caratteri=0
#for linea in linee:
#    caratteri +=len(linea)
print("caratteri:", len(alice))
print("caratteribbb:", notblank)
print("alf:", alfnum)