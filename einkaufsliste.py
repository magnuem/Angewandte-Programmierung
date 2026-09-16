einkauf = []

for i in range(5):
    print("Was musst du einkaufen?")
    artikel = input()
    einkauf.append(artikel)

einkauf.sort()
print("Deine Einkauf ist:")
for nummer, artikel in enumerate(einkauf, start=1):
    print(nummer, artikel)

print("Was möchtest du von der Liste streichen?")
einkauf.remove(input())

print("Deine Einkaufsliste ist jetzt:")
for nummer, artikel in enumerate(einkauf, start=1):
    print(nummer, artikel)

print(f"Auf deiner Einkaufsliste sind nun {len(einkauf)} Artikel.")