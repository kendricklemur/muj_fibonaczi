a=input("Ktory wyraz chcesz wyznaczyc?")
b=int(a)

while b<=0:
    print("Podaj numer wyrazu wiekszy od zera")
    a=input("Ktory wyraz chcesz wyznaczyc?")
    b=int(a)

wynik=0
ciag=[0,1]

for i in range(2,b+1):
    wynik=ciag[i-1] + ciag[i-2]
    ciag.append(wynik)

print(wynik)