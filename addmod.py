import psycopg2

id = input("ID: ")
name = input("Naam: ")
email = input("Email: ")
connection_string = "host='localhost' dbname='proja' user='postgres' password='PW'"

conn = psycopg2.connect(connection_string) 
cursor = conn.cursor()

query = """INSERT INTO moderator (modnummer, naam, email)
           VALUES (%s, %s, %s);"""      # Always use %s as a placeholder. Pyscopg will
                                        # convert the datatype and add quotes if necessary!
data = (id, name, email)
cursor.execute(query, data)             # The second parameter must be list or tuple
conn.commit()
conn.close()