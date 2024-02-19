import math

π = input('π:')     #3.1415     #assegno il valero di pi
print(π)

r1 = input('r1:')     #30        #assegno il valore del raggio del primo cerchio
print(r1)

r2 = input('r2:') #45        #assegno il valore del raggio del secondo cerchio
print(r2)

r3 = input('r3:') #33        #assegno il valore del raggio del terzo cerchio
print(r3)

h = input("h:")   #130        #assegno il valore dell'altezza
print(h)

S1 = π*r1**2   #calcolo l'area del primo cerchio

S2 = π*r2**2   #calcolo l'area del secondo cerchio

S3 = π*r3**2   #calcolo l'area del terzo cerchio

V = (1/6)* h*(S1 + 4*S2 + S3) #calcolo il volume della botte

liters = V / 1000 #converto il volume da cm3 in litri

print(liters)  #stampo il valore del volume in litri

A = 2*π*((r1 + r2)/2)h + π(r1*2 + r2*2)/2 #calcolo l'area totale del cilindro (botte)

print(A) #stampo il valore dell'area