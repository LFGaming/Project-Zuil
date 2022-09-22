#%%
name = str(input("Wat is je naam? "))
feedback = str(input("Wat was je ervaring met het station? "))

if name == "":
    print("Anoniem")
else:
    print("Naam " + name)

if len(feedback) >= 100:
    print("Te veel letters")
else:
    print("Gaf als feedback: " + feedback)
# %%
