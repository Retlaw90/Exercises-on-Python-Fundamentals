#Leggere da un file (persone.txt) i nomi, 
#cognomi e eta di un gruppo di persone.
#organizzarli in un dizionario la cui chiave è il cognome e il cui valore è 
#una t-upla contenente i tre valori letti.
fin = open("persone.csv", "r")
linee = fin.readlines()
fin.close()
for l in linee:
    l1=l.strip().split(",")
    print("Nome:",l1[0],"Cognome:",l1[1],"Età:",l1[2])
d=dict()
for l in linee:
    l1=l.strip().split(",")
    d[l1[0]] = (l1[0],l1[1],l1[2])
print(d)
for e in d:
    print("Key:", e, "Value:", d[e])