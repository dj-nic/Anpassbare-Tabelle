# Sehr wichtiger relevanter Kommentar für später oder so muss man dann ändern weil das sehr sehr wichtig ist sonst wird herr Kuhlmann sauer und das wollen wir nicht deswegen kommt hier ein guter kommentar hin.

# Input für die Breite der Tabelle als "n"
n = int(input("Gebe die Breite der Tabelle an"))
# Input für die Höhe der Tabelle als "p"
p = int(input("Gebe die Höhe der Tabelle an"))
for a in range (1,p+1):
    # Ergebnis='' ist hier noch "leer" um es anschließend für das ausgrechnete und das Print zu nutzen
    Ergebnis=''
    for k in range (1,n+1):
        Ergebnis=Ergebnis+str(a*k) + '\t'
    print (Ergebnis)
