import random
geheimzahl = random.randint(1, 50)

print("Salut!")
print("Rate, an welche Zahl ich gerade denke.")
print("Zwischen 1 und 50.")

guess = int(input())
count = 0

while guess != geheimzahl:
    if guess < geheimzahl:
        print("Zu tief!")
    elif guess > geheimzahl:
        print("Zu hoch!")

    guess = int(input("Nächster Versuch: "))
    count += 1

print("Jackpot!")
print(f"Du hast {count} Versuche gebraucht.")