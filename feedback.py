#%%
name = str(input("Wat is je naam? "))
feedback = str(input("Wat was je ervaring met het station? "))

if name == "":
    print("Anoniem")
else:
    print(f"Naam: {name}")

if len(feedback) >= 140:
    print("Te veel letters")
else:
    print(f"Gaf als feedback: {feedback}")
# %%
