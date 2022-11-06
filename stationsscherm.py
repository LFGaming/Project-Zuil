import tkinter as tk
import psycopg2

# get list of stations uit database
# get list of top 5 goedgekeurde berichten uit dbase
# convert svg to png: 
#  & 'C:\Program Files\Inkscape\bin\inkscape.exe'  -w 40 -h 40 .\ov-fiets--small.svg -o .\ov-fiets--small.png



def krijg_station_info(stationnum):
    global pr
    global wc
    global lift
    global ovfiets 
    global station
    connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = f"select * from station where stationnummer = {stationnum}"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    record = cursor.fetchone()
    station = record[1]
    pr = record[2]
    wc = record[3]
    lift = record[4]
    ovfiets = record[5]
    conn.commit()
    conn.close()
    window.update()

def berichten():
    global frm_berichten
    connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = f"select * from bericht where beoordeling = 'goed' order by tijd limit 5"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        tk.Label(frm_berichten, text=f"{row[2]}",  font=("Arial", 16) , width=100).pack()
        tk.Label(frm_berichten, text=f"- {row[1]}\t\t\n", font=("Arial", 16, "italic"), anchor="e", width = 100 ).pack()

    conn.commit()
    conn.close()

def volgendstation():
    global gekozen_station
    gekozen_station = (gekozen_station +1)
    if gekozen_station > 3:
        gekozen_station = 1
    print(station)
    krijg_station_info(gekozen_station)
    update_screen()

def vorigstation():
    global gekozen_station
    gekozen_station = (gekozen_station -1)
    if gekozen_station < 1:
        gekozen_station = 3
    print(gekozen_station)
    krijg_station_info(gekozen_station)
    update_screen()




def update_screen():
    global frm_content
    global frm_berichten

    btn_left = tk.Button(frm_content, command=vorigstation ,text="<", font=("Arial", 16, "bold"))
    btn_right = tk.Button(frm_content, command=volgendstation, text=">", font=("Arial", 16, "bold"))
    lbl_station = tk.Label(frm_content, text=f"Station: {station}", font=("Arial", 25)) 

    btn_left.grid(row=0, column=0,  padx=5, pady=5)
    lbl_station.grid(row=0, column=1,columnspan=2, padx=5, pady=5)
    btn_right.grid(row=0, column=3,  padx=5)

    # berichten frame
    frm_berichten = tk.Frame(frm_content, relief=tk.RAISED, borderwidth=2, height=300, bg='red')
    frm_berichten.grid(row=1, column=0, columnspan=4, sticky='ew')
    berichten()

    # frame twee kolommen voor voorzieningen en weer

    frm_voorzieningen = tk.Frame(frm_content)
    frm_voorzieningen.grid(row=2, column=0, columnspan=2, sticky= 'nw')
    tk.Label(frm_voorzieningen, text="Voorzieingen op dit station", font=("Arial", 16), anchor="n").pack() 

    img_ov = tk.PhotoImage(file='icons\img_ovfiets.png')

    tk.Label( frm_voorzieningen, image=img_ov).pack(side=tk.LEFT)
    tk.Label( frm_voorzieningen, text="OV fiets").pack(side=tk.LEFT, padx=20)

    frm_weer = tk.Frame(frm_content )
    frm_weer.grid(row=2, column=2, columnspan=2, sticky= 'nw')
    frm_weer.columnconfigure(0, weight=1)

    tk.Label(frm_weer, text="Weersvoorspelling", font=("Arial", 16), anchor="nw").pack() 

    img_zon = tk.PhotoImage(file='icons\weather\clear.png')

    tk.Label( frm_weer, image=img_zon).pack(side=tk.LEFT)
    tk.Label( frm_weer, text="Mooi weer\n10 graden\nGeen regen").pack(side=tk.LEFT, padx=20)


window = tk.Tk()
window.title("Stationsscherm")
#window.iconbitmap("yourimage.ico")

# Globale variabelen voor de stationsgegevens - die worden geupdate als je < of > kiest
gekozen_station = 1
pr = False
wc = False
lift = False
ovfiets = False
station = ""

frm_content = tk.Frame(window)
frm_content.grid(column=0, row=0)

krijg_station_info(gekozen_station)
update_screen()
window.mainloop()