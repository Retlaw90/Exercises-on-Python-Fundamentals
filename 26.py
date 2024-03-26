import copy
import random


# Genera una lista che contiene M numeri casuali tra 1 e N
def GeneraLista(N, M):
    lista = []
    for i in range(M):
        v = random.randint(1, N)
        lista.append(v)
    return lista


def ContaUgualiInStessoEInAltro(ls, lsCheck):
    ls = ls.copy()
    lsCheck = lsCheck.copy()
    # Conteggio e elimino gli elementi nello stesso posto
    stessoPosto = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            stessoPosto += 1
            ls[i] = None
            lsCheck[i] = None

    # Conteggio e elimino gli elementi in posto differente
    altroPosto = 0
    for v in lsCheck:
        if v != None and v in ls:
            altroPosto += 1
            ls.remove(v)
    return stessoPosto, altroPosto


N = int(input("Inserire il numero di simboli: "))
M = int(input("Inserire la lunghezza della lista: "))
l1 = GeneraLista(N, M)
l2 = GeneraLista(N, M)
print(l1)
print(l2)
strike, ball = ContaUgualiInStessoEInAltro(l1, l2)
print(strike, ball)
print(l1)
print(l2)


def ConvertiStringaDigitInListaNumeri(sd):
    return [int(x) for x in list(sd)]


# Esempio di utilizzo:
sd = input("Inserisci la tua prova: ")
print(ConvertiStringaDigitInListaNumeri(sd))




