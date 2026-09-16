class Konto:
    anzahl_konten = 0

    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.kontostand = kontostand
        Konto.anzahl_konten += 1

    def begruessen(self):
        print(f"Hallo {self.inhaber}.")

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag
        else:
            print("Nicht genug Guthaben.")

    def kontostand_anzeigen(self):
        print(f"Kontostand: {self.kontostand}")