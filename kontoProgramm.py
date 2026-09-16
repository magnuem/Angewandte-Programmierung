from konto import Konto

konto1 = Konto("Salome", 12000)

while True:
    print(f"Hallo. Was möchtest du machen?")
    print("1: Einzahlen")
    print("2: Abheben")
    print("3: Kontostand anzeigen")
    print("4: Beenden")

    auswahl = input()

    if auswahl == "1":
        betrag = int(input("Wie viel möchtest du einzahlen? "))
        konto1.einzahlen(betrag)

    elif auswahl == "2":
        betrag = int(input("Wie viel möchtest du abheben? "))
        konto1.abheben(betrag)

    elif auswahl == "3":
        konto1.kontostand_anzeigen()

    elif auswahl == "4":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Eingabe.")