print("Bitte schreibe einen Satz:")
satz = input()

words_list = satz.split()
words = {}

for i in words_list:
    if i in words:
        # Falls Wort schon in Dictionary, Zähler erhöhen
        words[i] = words[i] + 1

    else:
        # Wort ist noch nicht im Dictionary
        # Wort speichern und zählen mit 1
        words[i] = 1

print("So oft kommen die Wörter vor:")

for wort, wert in words.items():
    print(wort, ":", wert)