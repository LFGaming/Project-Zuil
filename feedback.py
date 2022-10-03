#%%
name = str(input("Wat is je naam? (optioneel) "))
feedback = str(input("Wat was je ervaring met het station? "))

def response(name, feedback):
    if name == "":
        print("Anoniem")
    else:
        print(f"Naam: {name}")

    if len(feedback) >= 140:
        print("Te veel letters")
    else:
        print(f"Gaf als feedback: {feedback}")

    with open('scheldwoorden.txt', 'r') as f:
        if feedback in f.read():
            print("Er zit een scheldwoord in de feedback of de naam, het wordt naar de check gestuurd")
            with open('feedback_check.txt', 'a') as g:
                g.write(f"Naam: {name} \nFeedback: {feedback}\n \n --------------------------- \n")
        else:
            with open('feedbacks.txt', 'a') as t:
                t.write(f"Naam: {name} \nFeedback: {feedback}\n \n --------------------------- \n")

r = response(name, feedback)

# scheldwoorden komen van https://www.dutchmultimedia.nl/scheldwoordenboek-1-000-den-nederlandse-scheldwoorden/
# %%
