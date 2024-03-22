def Somma(n):
    if n == 0:
        return 0
    else:
        return Somma(n - 1) + n


print(Somma(10))
# La ricorsione non va utilizzata in modo stupido
# Specialmente all'inizio la ricorsione non va utilizzata
# Se una funzione non è inerentemente ricorsiva, allora la devo implementare in modo iterativo


def Somma(n):
    totale = 0
    for i in range(n):
        totale += i
    return totale


def Prodotto(n):
    totale = 1
    for i in range(n):
        totale *= i
    return totale


l = [1, 5, 4, 8, 7, 6, 4, 3, 2]
totale = 0
for i in l:
    totale = totale + i

ls = ["Uno", "due", "tre", "quattro"]
# calcolare la somma delle lunghezze delle stringhe
totale = 0
for s in ls:
    totale = totale + len(s)

ls = [3, 2, 6, 7, 645, 7, 87, 7, 34, 324, 34, 6, 5, 6, 97, 9, 90]
# calcolare quanti numeri maggiori di 100 ci sono nella lista ls
totale = 0
for i in ls:
    if i > 100:
        totale = totale + 1

ls = [1, [2, 3], 3, "Ciao", "ok", 11, 1, 1, "aaa", 10, ["a", "b", "c"]]
# contare quante stringhe sono presenti nella lista ls
totale = 0
tipo_stringa = type("")
for i in ls:
    if type(i) == tipo_stringa:
        totale = totale + 1
print(totale)


ls = [3, 2, 6, 7, 645, 7, 87, 7, 34, 324, 34, 6, 5, 6, 97, 9, 90]


# scrivere una funzione che calcola quanti numeri maggiori di 100 ci sono nella lista ls
def Conta100(ls):
    totale = 0
    for i in ls:
        if i > 100:
            totale = totale + 1
    return totale


Conta100([1, 2, 3333, 4445, 666])


# somma => sottrazione,
# prodotto=> somma,
# divisione=>prodotto,
# sottrazione=> divisione


# 2 * 10 + 4
def Somma(a, b):
    return a - b


def Prodotto(a, b):
    return a + b


def Divisione(a, b):
    return a * b


def Sottrazione(a, b):
    return a / b


print(Somma(Prodotto(2, 10), 4))
