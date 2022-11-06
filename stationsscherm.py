import tkinter as tk

# get list of stations uit database
# get list of top 5 goedgekeurde berichten uit dbase
# convert svg to png: 
#  & 'C:\Program Files\Inkscape\bin\inkscape.exe'  -w 40 -h 40 .\ov-fiets--small.svg -o .\ov-fiets--small.png

window = tk.Tk()
window.title("Stationsscherm")
#window.iconbitmap("yourimage.ico")

# kies een van de stations
frm_content = tk.Frame(window)
frm_content.grid(column=0, row=0)
station= "Arnhem"
btn_left = tk.Button(frm_content, text="<", font=("Arial", 16, "bold"))
btn_right = tk.Button(frm_content, text=">", font=("Arial", 16, "bold"))
lbl_station = tk.Label(frm_content, text=f"Station: {station}", font=("Arial", 25)) 

btn_left.grid(row=0, column=0,  padx=5, pady=5)
lbl_station.grid(row=0, column=1,columnspan=2, padx=5, pady=5)
btn_right.grid(row=0, column=3,  padx=5)

# berichten frame
frm_berichten = tk.Frame(frm_content, relief=tk.RAISED, borderwidth=2, height=300, bg='red')
frm_berichten.grid(row=1, column=0, columnspan=4, sticky='ew')
lbl_bericht1 = tk.Label(frm_berichten, text="bericht 1 met nog een stukje tekst om uit te vullen",  font=("Arial", 16) , width=100)
lbl_naam = tk.Label(frm_berichten, text="- Anoniempje\t\t\n", font=("Arial", 16, "italic"), anchor="e", width = 100 )
lbl_bericht2 = tk.Label(frm_berichten, text="bericht 2 Dit is een mooi station zeg!! ", font=("Arial", 16), width = 100)
lbl_bericht3 = tk.Label(frm_berichten, text="Ik vind deze informatiezuil een erg goed initiatief. Kan ik eindelijk eens laten weten wat ik ervan vind...", font=("Arial", 16), width = 100)

lbl_bericht1.pack()
lbl_naam.pack()
lbl_bericht2.pack()
tk.Label(frm_berichten, text="- Anoniempje2\t\t\n", font=("Arial", 16, "italic"), anchor="e", width = 100 ).pack()
lbl_bericht3.pack()
tk.Label(frm_berichten, text="- Johan\t\t\n", font=("Arial", 16, "italic"), anchor="e", width = 100 ).pack()

# fram twee kolommen voor voorzieningen en weer

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

window.mainloop()