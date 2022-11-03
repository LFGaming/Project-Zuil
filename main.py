import tkinter as tk
import datetime
import random
import psycopg2

#id = input("Unique id: ")
#name = input("Name: ")
#bericht = input("Bericht: ")
#tijd = input("Tijd: ")


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

# Database

id = input("Unique id: ")
name = input1.get()
bericht = input2.get()
location = station
date = vandaag

connection_string = "host='localhost' dbname='proja' user='postgres' password='PW'"

conn = psycopg2.connect(connection_string) 
cursor = conn.cursor()

query = """INSERT INTO bericht (idnummer, naam, bericht, date, )
           VALUES (%s, %s, %s);"""      # Always use %s as a placeholder. Pyscopg will
                                        # convert the datatype and add quotes if necessary!
data = (id, name, bericht)#, tijd)
cursor.execute(query, data)             # The second parameter must be list or tuple
conn.commit()
conn.close()