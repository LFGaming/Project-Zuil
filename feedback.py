#%%
name = str(input("Wat is je naam? (optioneel) "))
feedback = str(input("Wat was je ervaring met het station? "))

if name == "":
    print("Anoniem")
else:
    print(f"Naam: {name}")

if len(feedback) >= 140:
    print("Te veel letters")
else:
    print(f"Gaf als feedback: {feedback}")

with open('scheldwoorden.txt') as f:
    if feedback in f.read():
        print("Er zit een scheldwoord in de feedback")

# scheldwoorden komen van https://www.dutchmultimedia.nl/scheldwoordenboek-1-000-den-nederlandse-scheldwoorden/
# %%
