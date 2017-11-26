'''
Created on 12.11.2017

@author: Marvin
'''
#from _operator import pos

def main():
    a = ['a','k','u','i','f','x','f']           # Liste mit Elementen
    b = []                                      # Leereliste
    c = []                                      # Leereliste
    d = [[],[]]                                 # Matrix
    
    for pos in a:                               # For-Schleife fuer alle Positionen/Elemente in del Liste a
        if pos == 'f':                          # Vergleich ob Element an Position pos ein f ist
            b.append(pos)                       # Scheibt Element an Position pos aus Liste a in die Liste b
    print(b)                                    # Ausgabe von Liste b
    
    
    for idx in range(len(a)):                   # For-Schleife mit dem Laufindex idx ueber den Bereich der Laenge der Liste a
        if a[idx] == 'f':                       # Vergleich ob Element an Position idx in Liste a ein f ist
            c.append(a[idx])                    # Scheibt das Element an Position idx aus Liste a in Liste c
    print(c)                                    # Ausgabe von Liste s
    
    for idx in range(0,len(a),1):               # For-Schleife mit dem Laufindex idx ueber den bereich von 0 bis Laenge von a mit der Schrittweite 1
        print(idx)                              # Ausgabe des Laufindex idx
        if a[idx] == 'f':                       # Vergleich ob Element an Position idx in Liste a ein f ist
            d[0].append(idx)                    # Speichern des Wertes von idx in der ersten Splate der Matrix
            d[1].append(a[idx])                 # Speichern des Elements an Position idx aus Liste a in der zweiten Spalte der Matrix
    print(d)                                    # Gibt automatisch erst die erste Spalte der Matrix d aus und dann die 2.
    
if __name__ == '__main__':                      # Ueberprueft ob Aufruf direckt erfolgt oder ueber ein anderes Skript
    main()                                      # Aufruf der definierten main() Funktion