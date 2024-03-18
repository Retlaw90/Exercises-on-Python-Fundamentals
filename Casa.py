import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
"""
print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])
"""

# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...
"""
#Esempio:
InItalia = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in InItalia.keys():
        InItalia[v["Team"]]=InItalia[v["Team"]]+1
    else:
        InItalia[v["Team"]]=1

print(InItalia)
"""

Country = dict()
for i in worldcup:
    if i["ClubCountry"] in Country.keys():
        Country[i["ClubCountry"]]=Country[i["ClubCountry"]]+1
    else:
        Country[i["ClubCountry"]]=1

print(Country)

lista=list(Country)
print(lista)
"""
ita=Country.get("Italy")
print("Giocatori che hanno giocato in italia:",ita)

brasile=Country.get("Brazil")
print("Giocatori che hanno giocato in Brasile:",brasile)

Argentina=Country.get("Argentina")
print("Giocatori che hanno giocato in Argentina:",Argentina)

InOrdine = {k: v for k, v in sorted(Country.items(), key=lambda item: item[1], reverse=True)}
print(InOrdine)



worldcup=worldcup.dir{}
for Compleanno in worldcup.key:
    print(Compleanno)

print(listaW[8])
Compleanno=listaW.get("DateOfBirth")
print(Compleanno)


print(Compleanno)
Giovane=max(Compleanno)
print(Giovane)

Vecchio= min (Compleanno)
print(Vecchio)
"""