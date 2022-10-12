import tkinter as tk
from datetime import date

vandaag = date.today()

def response():
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
                    f"{vandaag}\nNaam: {input1.get()} \nFeedback: {input2.get()}\n \n --------------------------- \n")
        else:
            with open('feedbacks.txt', 'a') as t:
                t.write(
                    f"{vandaag}\nNaam: {input1.get()} \nFeedback: {input2.get()}\n \n --------------------------- \n")


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
          text='Show', command=response).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()


#r = response(input1, input2)
