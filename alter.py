print("Hallo! Wie ist dein Name?")
name = input()

print("Und wie alt bist du?")
age = input()

print(f"Hallo {name}!")

age = int(age)
if age < 18:
    print("Du bist minderjährig.")
elif age >= 18 and age <= 64:
    print("Du bist im arbeitsfähigen Alter.")
else:
    print("Du bist im Rentenalter.")