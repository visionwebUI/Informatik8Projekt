import random

print(f'Willkommen...')
print(f'Version 2.0')
print(f'...')

# Definition der Funktion "hoch"
def hoch(zahl1, zahl2):
    ergebnis = 1
    for _ in range(zahl2):
        ergebnis *= zahl1  # Multipliziere ergebnis jedes Mal mit zahl1
    return ergebnis

# Zwei Zufallszahlen generieren

x = random.randint(2, 25) #X Wert wird erzeugt
y = random.randint(2, 25) #Y Wert wird erzeugt

print(f"Zufallszahlen: x = {x}, y = {y}")
print(f"...")

# Die Einzelnen Hochrechnungsergebnisse werden in In den Variablen Gleichgesetzt
ergebnis1 = hoch(x, y)
ergebnis2 = hoch(y, x)

if ergebnis1 > ergebnis2:
    print(f"{x} hoch {y} ({ergebnis1}) ist größer als {y} hoch {x} ({ergebnis2}).")
elif ergebnis1 < ergebnis2:
    print(f"{y} hoch {x} ({ergebnis2}) ist größer als {x} hoch {y} ({ergebnis1}).")
else:
    print(f"{x} hoch {y} ({ergebnis1}) ist gleich {y} hoch {x} ({ergebnis2}).")

# Zusatzaufgabe: 10 Zufallszahlen werden erzeugen und 90 Kombinationen verglichen
zahlen = [random.randint(2, 25) for _ in range(10)]
max_ergebnis = float('-inf')
min_ergebnis = float('inf')
max_kombination = ()
min_kombination = ()

for i in range(len(zahlen)):
    for j in range(len(zahlen)):
        if i != j:  # Vermeiden, dass eine Zahl mit sich selbst hochgenommen wird
            ergebnis = hoch(zahlen[i], zahlen[j])
            if ergebnis > max_ergebnis:
                max_ergebnis = ergebnis
                max_kombination = (zahlen[i], zahlen[j])
            if ergebnis < min_ergebnis:
                min_ergebnis = ergebnis
                min_kombination = (zahlen[i], zahlen[j])

print(f"Die 10 Zufallszahlen sind: {zahlen}")
print(f"Das größte Ergebnis ist {max_ergebnis}, erzielt durch {max_kombination[0]} hoch {max_kombination[1]}.")
print(f"Das kleinste Ergebnis ist {min_ergebnis}, erzielt durch {min_kombination[0]} hoch {min_kombination[1]}.")

print(f'Code erfolgreich abgeschlossen. Bis zum nächsten Mal!')
