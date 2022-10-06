import tkinter as tk


def show_entry_fields():
    print(f"First Name: {input1.get()} \nLast Name: {input2.get()}")
    if input1.get() == "":
        print("Anoniem")
    else:
        print(f"Naam: {input1.get()}")

    if len(input2.get()) >= 140:
        print("Te veel letters")
    else:
        print(f"Gaf als feedback: {input2.get()}")

    with open('scheldwoorden.txt', 'r') as f:
        if input2.get() in f.read():
            print(
                "Er zit een scheldwoord in de feedback of de naam, het wordt naar de check gestuurd")
            with open('feedback_check.txt', 'a') as g:
                g.write(
                    f"Naam: {input1.get()} \nFeedback: {input2.get()}\n \n --------------------------- \n")
        else:
            with open('feedbacks.txt', 'a') as t:
                t.write(
                    f"Naam: {input1.get()} \nFeedback: {input2.get()}\n \n --------------------------- \n")

# name = str(input("Wat is je naam? (optioneel) "))
# feedback = str(input("Wat was je ervaring met het station? "))


'''def response(name, feedback):
    if name == "":
        print("Anoniem")
    else:
        print(f"Naam: {name.get()}")

    if len(feedback.get()) >= 140:
        print("Te veel letters")
    else:
        print(f"Gaf als feedback: {feedback.get()}")

    with open('scheldwoorden.txt', 'r') as f:
        if feedback.get() in f.read():
            print(
                "Er zit een scheldwoord in de feedback of de naam, het wordt naar de check gestuurd")
            with open('feedback_check.txt', 'a') as g:
                g.write(
                    f"Naam: {name.get()} \nFeedback: {feedback.get()}\n \n --------------------------- \n")
        else:
            with open('feedbacks.txt', 'a') as t:
                t.write(
                    f"Naam: {name.get()} \nFeedback: {feedback.get()}\n \n --------------------------- \n")'''


master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)

input1 = tk.Entry(master)
input2 = tk.Entry(master)

input1.grid(row=0, column=1)
input2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
'''tk.Button(master,
          text='test', command=response(input1, input2)).grid(row=4,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)'''


tk.mainloop()


#r = response(input1, input2)
