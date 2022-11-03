import tkinter as tk
import datetime
import random
import psycopg2

vandaag = datetime.datetime.today()

with open("stations.txt","r") as file:
    lines = file.read().splitlines()
    station = random.choice(lines)

name = str(input("Wat is je naam? (optioneel) "))
feedback = str(input("Wat was je ervaring met het station? "))


#name = input("Naam: ")
#bericht = input("Bericht: ")
stationnaam = str(station)
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
                "Er zit een scheldwoord in de feedback of de naam, het wordt afgekeurt.")
        else:
            # put message in database

            connection_string = "host='localhost' dbname='proja' user='postgres' password='PW'"

            conn = psycopg2.connect(connection_string) 
            cursor = conn.cursor()

            query = """INSERT INTO bericht (naam, bericht, stationnaam, tijd)
                    VALUES (%s, %s, %s, %s);"""      # Always use %s as a placeholder. Pyscopg will
                                                    # convert the datatype and add quotes if necessary!
            data = (name, feedback, stationnaam, tijd)
            cursor.execute(query, data)             # The second parameter must be list or tuple
            conn.commit()
            conn.close()

            #with open('feedbacks.txt', 'a') as t:
            #    t.write(
            #        f"{vandaag}\nBij station {station}\nNaam: {name} \nFeedback: {feedback}\n \n --------------------------- \n")


r = response()

# get message from database
def read():
    connection_string = "host='localhost' dbname='proja' user='postgres' password='PW'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = "select * from bericht"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("Naam = ", row[0])
        print("Bericht  = ", row[1])
        print("Tijd = ", row[2])
        print("Modnummer = ", row[3])
        print("Stationnaam = ", row[4], "\n")
    conn.commit()
    conn.close()

re = read()