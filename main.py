import tkinter as tk
import datetime
import random
import psycopg2


connection_string = "host='localhost' dbname='fabriek' user='postgres' password='geheim'"
conn = psycopg2.connect(connection_string)  # get a connection with the database
cursor = conn.cursor() # 


vandaag = datetime.datetime.today()

with open("stations.txt","r") as file:
    lines = file.read().splitlines()
    station = random.choice(lines)

def response():
    print(f"First Name: {input1.get()} \n Feedback: {input2.get()}")
    if input1.get() == "":
        print("Anoniem")
    else:
        print(f"Naam: {input1.get()}")

    if len(input2.get()) >= 140:
        print("Te veel letters")
    else:
        print(f"Gaf als feedback: {input2.get()}")

    with open('scheldwoorden_kort.txt', 'r') as f:
        if input2.get() in f.read():
            print(
                "Er zit een scheldwoord in de feedback of de naam, het wordt naar de check gestuurd")
            with open('feedback_check.txt', 'a') as g:
                g.write(
                    f"{vandaag}\nBij station {station}\nNaam: {input1.get()} \nFeedback: {input2.get()}\n \n --------------------------- \n")
        else:
            with open('feedbacks.txt', 'a') as t:
                t.write(
                    f"{vandaag}\nBij station {station}\nNaam: {input1.get()} \nFeedback: {input2.get()}\n \n --------------------------- \n")


master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Feedback").grid(row=1)

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
