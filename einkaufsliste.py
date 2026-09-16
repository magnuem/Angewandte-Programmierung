einkauf = []

for i in range(5):
    print("Was musst du einkaufen?")
    artikel = input()
    einkauf.append(artikel)

einkauf.sort()
print(f"Dein Einkauf ist: {einkauf}.")

print("Was möchtest du von der Liste streichen?")
überflüssig = input()
einkauf.remove(überflüssig)

print(f"{überflüssig} wird gestrichen.")
print(f"Deine Einkaufsliste ist jetzt: {einkauf}.")
print(f"Auf deiner Einkaufsliste sind nun {len(einkauf)} Artikel.")