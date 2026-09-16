telefonbuch = {
    "Salome": "0712345678",
    "Daniel": "0716452736",
    "Fabio": "0717463746"
}

print("Wie ist dein Name?")
name = input()

if name in telefonbuch:
    print(f"Deine Telefonnummer ist: {telefonbuch[name]}")
else:
    print("Deine Nummer ist nicht im Telefonbuch.")

print("Möchtest du eine neue Telefonnummer speichern? [Y/N]")
antwort = input()

while antwort != "Y" and antwort != "N":
    print("Bitte wähle Ja (Y) oder Nein (N).")
    antwort = input()

if antwort == "Y":
    print("Wie ist dein Name?")
    name = input()

    print("Wie lautet deine Telefonnummer?")
    number = input()

    telefonbuch[name] = number
    print("Telefonnummer wurde gespeichert.")

    print(f"Das Telefonbuch enthält nun:")
    for telefonbuch, wert in telefonbuch.items():
        print(telefonbuch, ":", wert)

elif antwort == "N":
    print("Auf Wiedersehen.")