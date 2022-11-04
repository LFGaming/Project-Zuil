import psycopg2

def read():
    connection_string = "host='localhost' dbname='proja' user='postgres' password='PW'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = "select * from bericht"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    print("Selecting rows from mobile table using cursor.fetchall")
    records = cursor.fetchall()

    print("Print each row and it's columns values")
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