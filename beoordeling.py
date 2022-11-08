import psycopg2
import datetime

# login with name and get the modnumber
def inloggen():
    
    name = str(input("Naam: "))

    # zoek of deze naam voorkomt in de database:
    connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = "select * from moderator where naam = %s"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    arg = (name, )
    cursor.execute(query, arg)
    records = cursor.fetchone()
    if len(records) == 0:
        print("U bent nog niet geregistreerd als moderator. Gebruik addmod.py \n")
        return -1
    else:
        print(f"Welkom {name} met email: {records[2]} \n")
        modnum = records[0]
        return modnum

# select if the shown message is allowed or not
def beoordeel(mod):
    connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = "select * from bericht where beoordeling is null"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("Geen nieuwe berichten")
    else:
        print("Te beoordelen berichten: ")

    for row in records:
        print("IDnummer = ", row[0])
        print("Naam = ", row[1])
        print("Bericht  = ", row[2])
        print("Tijd = ", row[3])
        print("Modnummer = ", row[4])
        print("Stationnaam = ", row[5], "\n")
        keuze = input("Goed of fout? (g of f): ")
        if keuze == 'g':
            # if message is allowed send update the database
            tijd = datetime.datetime.today()
            query = """update bericht set beoordeling = 'goed', modnummer = %s, beoordeling_tijd = %s where idnummer = %s"""
            arg = (mod, tijd, str(row[0]))
            cursor.execute(query, arg)             # The second parameter must be list or tuple
            conn.commit()

        else:
            # if the message is not allowed send update to the database
            tijd = datetime.datetime.today()
            query = """update bericht set beoordeling = 'fout', modnummer = %s, beoordeling_tijd = %s where idnummer = %s"""
            arg = (mod, tijd, str(row[0]))
            cursor.execute(query, arg)             # The second parameter must be list or tuple
            conn.commit()

    conn.close()

mod = inloggen()
if mod != -1:
    beoordeel(mod)