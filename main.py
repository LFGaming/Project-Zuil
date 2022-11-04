import tkinter as tk
import datetime
import random
import psycopg2

vandaag = datetime.datetime.today()

#with open("stations.txt","r") as file:
#    lines = file.read().splitlines()
#    station = random.choice(lines)

name = str(input("Wat is je naam? (optioneel) "))
feedback = str(input("Wat was je ervaring met het station? "))


#name = input("Naam: ")
#bericht = input("Bericht: ")
stationnummer = random.randint(1,3)
tijd = str(vandaag)

def response():
    print(f"First Name: {name} \n Feedback: {feedback}")
    if name == "":
        print("Anoniem")
    else:
        print(f"Naam: {name}")

    if len(feedback) >= 140:
        print("Te veel letters")
    else:
        print(f"Gaf als feedback: {feedback}")

    with open('scheldwoorden_kort.txt', 'r') as f:
        if feedback in f.read():
            print(
                "Er zit een scheldwoord in de feedback of de naam, het wordt afgekeurd.")
        else:
            # put message in database

            connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

            conn = psycopg2.connect(connection_string) 
            cursor = conn.cursor()

            query = """INSERT INTO bericht (naam, bericht, stationnummer, tijd)
                    VALUES (%s, %s, %s, %s);"""      # Always use %s as a placeholder. Pyscopg will
                                                    # convert the datatype and add quotes if necessary!
            data = (name, feedback, stationnummer, tijd)
            cursor.execute(query, data)             # The second parameter must be list or tuple
            conn.commit()
            conn.close()

            #with open('feedbacks.txt', 'a') as t:
            #    t.write(
            #        f"{vandaag}\nBij station {station}\nNaam: {name} \nFeedback: {feedback}\n \n --------------------------- \n")


r = response()

# get message from database
def read():
    connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = "select * from bericht"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    records = cursor.fetchall()

    print("Berichten")
    for row in records:
        print("IDnummer = ", row[0])
        print("Naam = ", row[1])
        print("Bericht  = ", row[2])
        print("Tijd = ", row[3])
        print("Modnummer = ", row[4])
        print("Stationnaam = ", row[5], "\n")
    conn.commit()
    conn.close()

re = read()