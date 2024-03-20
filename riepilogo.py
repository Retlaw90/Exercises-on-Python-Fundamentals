# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!
# Il problema. Cosa fare?
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
# 10)Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

# Cosa fare?
"""
1) leggere i dati (importare i dati nel programma)
2) organizzare i dati in modo opportuno (nel nostro caso sono già organizzati come elenco di calciatori, con un insieme di proprietà per ogni calciatore)
3) per ogni richiesta il cosa constiste in un conteggio oppure nella ricerca di condizioni specifiche
"""

# Per prima cosa leggiamo il file, essendo json utilizziamo le librerie JSON
import json

# Per leggere un file json
filejson = open(
    "all-world-cup-players.json",
    "r",
)
worldcup = json.load(filejson)
filejson.close()

"""
al simbolo worldcup ho associato una lista (la json.load) torna un elemento json che in questo caso corrisponde a una lista (delimitato da [])
"""
# Di che tipo è worldcup?
# Di che tipo sono gli elementi di worldcup?
print(type(worldcup))
print(type(worldcup[0]))

# exit(-1) # per non eseguire le istruzioni successive

# 1) contare quanti calciatori hanno giocato per l'Italia
# come? per ogni calciatore (cioè per ogni elemento della lista wordcup), se il calciatore appartiene al team ITA, lo conteggio
# Variabili? totaleCalciatoriItalia

# Inizializzo il contatore a 0
totaleCalciatoriItalia = 0
# Per ogni calciatore....
for c in worldcup:
    # devo verificare che il team sia ITA oppure Italy
    # if c["Team"] in ["ITA", "Italy"]:
    if c["Team"] == "ITA" or c["Team"] == "Italy":
        totaleCalciatoriItalia += 1
# Ho sbagliato, non ho tenuto conto dei requisiti!! Voglio solo i calciatori "diversi" invece in questo modo ho contato i duplicati
"""
Quindi dovrò
1) prendere tutti i calciatori che hanno giocato per l'italia
2) eliminare i duplicati
3) contare i duplicati
"""
calciatoriItalia = []
# Per ogni calciatore....
for c in worldcup:
    # devo verificare che il team sia ITA oppure Italy
    if c["Team"] in ["ITA", "Italy"]:
        # if c["Team"] == "ITA" or c["Team"] == "Italy":
        calciatoriItalia.append(c["FullName"])
calciatoriItaliaSenzaRipetizioni = set(calciatoriItalia)
print("Calciatori italiani: ", len(calciatoriItaliaSenzaRipetizioni))


# 2) contare quanti calciatori hanno giocato per il Brasile
calciatoriBrasile = []
for c in worldcup:
    if c["Team"] in ["BRA", "Brazil"]:
        calciatoriBrasile.append(c["FullName"])
calciatoriBrasileSenzaRipetizioni = set(calciatoriBrasile)
print("Calciatori brasiliani: ", len(calciatoriBrasileSenzaRipetizioni))

# 3) contare quanti calciatori hanno giocato per l'Argentina
# trivial!!!


# Ora al posto di fare sostanzialmente tre volte lo stesso codice, potrei scrivere una funzione
def ContaCalciatoriSquadra(elenco, squadra):
    calciatoriSquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatoriSquadra.append(c["FullName"])
    calciatoriSquadraSenzaRipetizioni = set(calciatoriSquadra)
    return len(calciatoriSquadraSenzaRipetizioni)


print("Calciatori italia: ", ContaCalciatoriSquadra(worldcup, ["ITA", "Italy"]))
print("Calciatori brasile: ", ContaCalciatoriSquadra(worldcup, ["BRA", "Brazil"]))
print("Calciatori argentina: ", ContaCalciatoriSquadra(worldcup, ["ARG", "Argentina"]))


# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
""" come?
1) ottengo l'elenco dei calciatori che hanno giocato per l'italia
2) ottengo l'elenco dei calciatori che hanno giocato per il brasile
3) per ogni calciatore che ha giocato per l'italia
    verifico se è presente nell'elenco dei calciatori che hanno giocato per il brasile
"""


# Se modifico la funzione ContaCalciatoriSquadra e tolgo la len, ottengo esattamente
# l'elenco dei giocatori che hanno giocato in una certa squadra
def CalciatoriSquadra(elenco, squadra):
    calciatoriSquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatoriSquadra.append(c["FullName"])
    calciatoriSquadraSenzaRipetizioni = set(calciatoriSquadra)
    return calciatoriSquadraSenzaRipetizioni


calciatoriItalia = CalciatoriSquadra(worldcup, ["ITA", "Italy"])
calciatoriBrasile = CalciatoriSquadra(worldcup, ["BRA", "Brazil"])
calciatoriArgentina = CalciatoriSquadra(worldcup, ["ARG", "Argentina"])

print("Calciatori italia e brasile: ", calciatoriItalia.intersection(calciatoriBrasile))
print( "Calciatori italia e argentina: ",calciatoriItalia.intersection(calciatoriArgentina))
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
"""
come?
1)ottengo una lista di date di compleanno
2)rimuovo dalla lista imperfezioni (spazio, date vuote)
3)spampo il max e il min
"""
#creo la lista date
Compleanno=[]
for Date in worldcup:
    Compleanno.append(Date["DateOfBirth"])
#elimini spazi e date vuote creando una lista di solo anno di nascita
year_list = [date.split('-')[0] for date in Compleanno]
Datepulite = [year.replace(' ', '') for year in year_list]
Anno = [year for year in Datepulite if year]
print(Anno)
#stampo l'anno piu' alto e basso della lista
print("Calciatore più anziano", max(Anno))
print("Calciatore più giovane:", min(Anno))

#8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
"""
1)contare per ogni giocatore quante volte è presente della lista
"""
#creo un dizionario che conta quante volte è presente il giocatore nell'anno
from collections import Counter
count_dict = {}

for item in worldcup:
    year = item["Team"]
    name = item["FullName"]
    if year not in count_dict:
        count_dict[year] = Counter()
    count_dict[year][name] += 1

print(count_dict)


# Troviamo il nome del giocatore con il conteggio più alto in tutti gli anni
max_count = 0
max_name = None
for year, counter in count_dict.items():
    name, count = counter.most_common(1)[0]
    if count > max_count:
        max_count = count
        max_name = name

print(f"Il giocatore che appare più volte è {max_name} con {max_count} apparizioni.")
#NOTA BENE, IL NOME DEL GIOCATORE è VUOTO
#9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
"""
1)contare per ogni squadra quante volte è presente il giocatore
"""
#creo un dizionario che conta quante volte è presente il giocatore nella squadra
Dirsqua = {}

for item in worldcup:
    Squadra = item["Team"]
    Nome = item["FullName"]
    if Squadra not in Dirsqua:
        Dirsqua[Squadra] = Counter()
    Dirsqua[Squadra][Nome] += 1

print(Dirsqua)


# Troviamo il nome del giocatore con il conteggio più alto
max_team = 0
max_nome = None
for team, counter in Dirsqua.items():
    name, count = counter.most_common(1)[0]
    if count > max_team:
        max_team = count
        max_nome = name

print(f"Il giocatore che appare più volte è {max_nome} con {max_team} apparizioni.")
#chiedere come mostrare il nome della squadra.

#chiedere del punto 10.

# 10)Organizzare per nazione. 
#Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, 
#quale squadra francese, ...
"""
conta per ogni giocatore quante volte è presente nella squadra
"""
from collections import defaultdict

# Creiamo un dizionario dove le chiavi sono le nazioni e i valori sono i conteggi dei giocatori
player_counts = defaultdict(int)

for player in worldcup:
    player_counts[player["ClubCountry"]] += 1

# Stampiamo il numero di giocatori per ogni nazione
for country, count in player_counts.items():
    print(f"{country}: {count} giocatori")












