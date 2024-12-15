import tkinter as tk
from PIL import Image, ImageTk  

def show(path, title):
    """Functie pentru deschiderea unei noi ferestre cu o imagine data"""
    window = tk.Toplevel() #Creaza fereastra secundara
    window.title(title) #Seteaza titlu

    img = Image.open(path) #Deschide imaginea de la o cale
    img = ImageTk.PhotoImage(img) #Seteaza imaginea intr-un format pentru Tkinter

    label = tk.Label(window, image=img) #Creaza un label pentru a afisa imaginea 
    label.image = img #Salveaza referinta, evitam ca imaginea sa fie eliminata din memorie
    label.pack() #Adauga label-ul in fereastra noastra secundara

#Urmatoarele 3 functii se folosesc de functia "show" pentru a crea ferestrele celor 3 grafice, cu caile lor specifice aflate deja in director
def show_all():
    show("all_values.png", "Toate valorile")

def show_first7():
    show("first7_values.png", "Primele 7 valori")

def show_last11():
    show("last11_values.png", "Ultimele 11 valori")

root = tk.Tk() #Creaza fereastra principala a Tkinter-ului
root.title("Afisare grafice!") #Seteaza titlul

#Urmatoarele 3 butoane ne afiseaza cele 3 imagini, astfel, root ne indica fereastra principala, text este textul de pe buton, iar command este functia apelata
tk.Button(root, text="Toate valorile", command=show_all).pack()
tk.Button(root, text="Primele 7 valori", command=show_first7).pack()
tk.Button(root, text="Ultimele 11 valori", command=show_last11).pack()

#Buton pentru inchiderea ferestrei principale
tk.Button(root, text="Iesire!", command=root.quit).pack()

root.mainloop() #Porneste bucla pentru fereastra principala, astfel asteapta interactiunea si actualizeaza interfanta cat timp fereastra nu este inchisa.
