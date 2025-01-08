import random

print(f'Willkommen...') #Der User wird über das erfolgreiche abschließen des Codes abgeschlossen
print(f'Version 2.0') #Es wird darüber Informiert das es sich um eine zweite Version handelt
print(f'...')
x = random.randint(2, 25) #X wird deffiniert
print(x) #X wird in die Konsole Geschrieben
y = random.randint(2, 25) #Y wird deffiniert
print(y) #Y wird in die Konsole Geschrieben
print(f'...')
ergebnis = 1

# Schleife, die Y-mal durchläuft
for _ in range(y):
    ergebnis *= x  # Multipliziere ergebnis jedes Mal mit X

# Ausgabe des Ergebnisses
print(f"{x} hoch {y} ist {ergebnis}")
print(f'Code erfolgreich abgeschlossen. Bis zum nächsten mal!')
