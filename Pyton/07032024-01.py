import random
import time

"""# Costruzione della lista
start = time.time_ns()
lista = []
for v in range(1, 1000):
    lista.append(random.randint(1, 100000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

# Ricerca nella lista
start = time.time_ns()
trovati = 0
for v in range(1, 10):
    if random.randint(1, 100000000000) in lista:
        trovati += 1
end = time.time_ns()

print(
    f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
)"""

########################################################################################
# Costruzione del set
start = time.time_ns()
aSet = set()
for v in range(1, 1000000):
    aSet.add(random.randint(1, 100000000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

# Ricerca nella lista
start = time.time_ns()
trovati = 0
for v in range(1, 10):
    if random.randint(1, 100000000000) in aSet:
        trovati += 1
end = time.time_ns()

print(
    f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
)
