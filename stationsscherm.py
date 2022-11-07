import tkinter as tk
import psycopg2
import requests, json

# get information of the station
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

# get the messages from the database
# set the messages on the screen
def berichten():
    global frm_berichten
    connection_string = "host='localhost' dbname='proja' user='postgres' password='Postgresqlekul!1'"

    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor()

    query = f"select * from bericht where beoordeling = 'goed' order by tijd desc limit 5"      # Always use %s as a placeholder. Pyscopg will
                                            # convert the datatype and add quotes if necessary!
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        tk.Label(frm_berichten, text=f"{row[2]}",  font=("Arial", 16) , width=100).pack()
        tk.Label(frm_berichten, text=f"- {row[1]}\t\t\n", font=("Arial", 16, "italic"), anchor="e", width = 100 ).pack()

    conn.commit()
    conn.close()

# functionality for the next (right) button
def volgendstation():
    global gekozen_station
    gekozen_station = (gekozen_station +1)
    if gekozen_station > 3:
        gekozen_station = 1

    krijg_station_info(gekozen_station)
    update_screen()

#functionality for the previouse (left) button
def vorigstation():
    global gekozen_station
    gekozen_station = (gekozen_station -1)
    if gekozen_station < 1:
        gekozen_station = 3

    krijg_station_info(gekozen_station)
    update_screen()

# get weather from openweathermap
# adding onto https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/ code
def weather(stad):
    global current_temperature, current_pressure, current_humidity, weather_description

    # Enter your API key here
    api_key = "c13f1638dfe627b88033ae5f03ec93eb"
    
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
       
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + stad + "&units=metric" + "&lang=nl"

    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
 
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
    

# functionality to update the screen so all the text does not get written on top of each other
def update_screen():
    global current_temperature, current_pressure, current_humidity, weather_description
    global frm_content
    global frm_berichten
    global lbl_station, frm_weer, frm_voorzieningen
    global lbl_ovfiets, lbl_toilet, lbl_lift, lbl_pr, lbl_weer
    
    weather(station)

    # update station name lable 
    lbl_station.config(text=f"Station: {station}")

    # remove all lables
    if lbl_ovfiets:
        lbl_ovfiets.destroy()
    if lbl_toilet:
        lbl_toilet.destroy()
    if lbl_pr:
        lbl_pr.destroy()
    if lbl_lift:
        lbl_lift.destroy()

    # put the right pictures on screen.
    if ovfiets:
        lbl_ovfiets = tk.Label( frm_voorzieningen, image=img_ov)
        lbl_ovfiets.pack(side=tk.LEFT, padx=10)
        
    if lift:
        lbl_lift = tk.Label( frm_voorzieningen, image=img_lift)
        lbl_lift.pack(side=tk.LEFT, padx=10)

    if pr:
        lbl_pr = tk.Label( frm_voorzieningen, image=img_pr)
        lbl_pr.pack(side=tk.LEFT, padx=10)

    if wc:
        lbl_toilet = tk.Label( frm_voorzieningen, image=img_toilet)
        lbl_toilet.pack(side=tk.LEFT, padx=10)

    # update the weather text
    lbl_weer.config(text = f"{weather_description}\n{current_temperature} graden C")

# setup the window that you see.
def initialise_screen():
    global current_temperature, current_pressure, current_humidity, weather_description
    global frm_content
    global frm_berichten
    global lbl_station, frm_weer, frm_voorzieningen
    global lbl_ovfiets, lbl_toilet, lbl_lift, lbl_pr, lbl_weer

    weather(station)

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
    tk.Label(frm_voorzieningen, text="Voorzieingen op dit station", font=("Arial", 16), anchor="w").pack() 



    if ovfiets:
        lbl_ovfiets = tk.Label( frm_voorzieningen, image=img_ov)
        lbl_ovfiets.pack(side=tk.LEFT, padx=10)
    if lift:
        lbl_lift = tk.Label( frm_voorzieningen, image=img_lift)
        lbl_lift.pack(side=tk.LEFT, padx=10)
    if pr:
        lbl_pr = tk.Label( frm_voorzieningen, image=img_pr)
        lbl_pr.pack(side=tk.LEFT, padx=10)
    if wc:
        lbl_toilet = tk.Label( frm_voorzieningen, image=img_toilet)
        lbl_toilet.pack(side=tk.LEFT, padx=10)


    frm_weer = tk.Frame(frm_content )
    frm_weer.grid(row=2, column=2, columnspan=2, sticky= 'nw')
    frm_weer.columnconfigure(0, weight=1)

    tk.Label(frm_weer, text="Weersvoorspelling", font=("Arial", 16), anchor="nw").pack() 

    tk.Label( frm_weer, image=img_weather).pack(side=tk.LEFT)
    lbl_weer = tk.Label( frm_weer, text=f"{weather_description}\n{current_temperature} graden C",  font=("Arial", 16))
    lbl_weer.pack(side=tk.LEFT, padx=20)

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
# de icoontjes die we gebruiken
img_ov = tk.PhotoImage(file='icons\img_ovfiets.png')
img_pr = tk.PhotoImage(file='icons\img_pr.png')
img_toilet = tk.PhotoImage(file='icons\img_toilet.png')
img_lift = tk.PhotoImage(file='icons\img_lift.png')
img_weather = tk.PhotoImage(file='icons\light-clouds.png')
lbl_pr = None
lbl_lift = None
lbl_ovfiets = None
lbl_toilet = None


frm_content = tk.Frame(window)
frm_content.grid(column=0, row=0)

krijg_station_info(gekozen_station)

initialise_screen()
window.mainloop()