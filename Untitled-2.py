zahl1 = int(input("Geben Sie eine Zahl ein: "))
zahl2 = int(input("Geben Sie eine weitere Zahl ein: "))
zahlen = [zahl1, zahl2]
zahlen.sort()

#For Schleife wie ich sie machen würde:
ergebnis = 0
for zahl in zahlen:
    ergebnis += zahl
print(ergebnis)

#Alternativ mit range:
ergebnis = 0
for zahl in range(len(zahlen)):
    ergebnis += zahlen[zahl]
print(ergebnis)

#while:
ergebnis = 0
zahl = 0
while zahl <len(zahlen):
   ergebnis += zahlen[zahl]
   zahl+=1
print(ergebnis)