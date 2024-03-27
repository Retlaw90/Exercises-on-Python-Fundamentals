# Ricordando che il MCD tra due numeri è il più grande numero che divide
# i due numeri dati, scrivere un programma che calcola il MCD tra due numeri
# letti da input
# Rcordate!!! dati A e B, se esiste un numero M che li divide, allora lo stesso
# numero dividerà A-B e B oppure B-A e A a seconda che A sia maggiore di
# B o che B sia maggiore di A
# Questa definizione, insieme alla considerazione che MCD(A,A)=A,
# ci consente di definire una soluzione che converge,
# garantendo la terminazione dell'algoritmo
# esempio
"""
MCD(38, 24)=
MCD(38-24, 24)=
MCD(14, 24)=
MCD(14, 24-14)=
MCD(14, 10)=
MCD(14-10, 10)=
MCD(4, 10)=
MCD(4, 10-4)=
MCD(4,6)=
MCD(4, 6-4)=
MCD(4,2)=
MCD(4-2,2)=
MCD(2,2)=2
"""


# Implementare la funzione MCD(A,B) che calcola il massimo comun divisore tra A e B#
a=int(input("Inserire a:"))
b=int(input("Inserire b:"))

def MCD(a, b):
  while a!=b:
    if a > b:
      a= a-b
    else:
       b= b-a
  return a
print(MCD(a,b))
