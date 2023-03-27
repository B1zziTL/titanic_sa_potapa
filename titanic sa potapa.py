#vlozenie modulu
import tkinter

#otvorenie suborov
subor = open("lodicky.txt","r")
subor1 = open("lodicky.txt","r")

#rozdelenie prveho riadku na medzerach
prvy_riadok = subor.readline()
prvy_riadocek = prvy_riadok.split()

#zadeklarovanie premennych a zoznamov
pocitadielko = 0
sirka = int(prvy_riadocek[0]) * 50
vyska = int(prvy_riadocek[1]) * 50
sirky = []
vysky = []

#vykreslenie platna
canvas = tkinter.Canvas(width=sirka, height=vyska, background="white")
canvas.pack()

def zistenie(): #funkcia na zistenie moznej polohy lodi
    #zadeklarovanie lokalnych premennych
    pocitadlo = 0
    stvorcek_x = 0
    stvorcek_y = 0

    #preskocenie prveho riadka suboru
    next(subor1)
    
    for riadok1 in subor1: #cyklus pre riadky v subore
        riadocek1 = riadok1.split()

        for slovo1 in riadocek1: #cyklus pre slova v riadku
            #podmienky na zistenie volneho miesta 
            if slovo1 == "0":
                pocitadlo += 1

            elif slovo1 != "0":
                pocitadlo = 0

            #podmienky na zapisanie pozicii volnych miest pre lodky
            if pocitadlo == 3:
                sirka_lodky = (stvorcek_x - 2) * 50
                vyska_lodky = stvorcek_y
                sirky.append(sirka_lodky)
                vysky.append(vyska_lodky)

            if pocitadlo == 7:
                sirka_lodky = (stvorcek_x - 2) * 50
                vyska_lodky = stvorcek_y
                sirky.append(sirka_lodky)
                vysky.append(vyska_lodky)

            #zmena pomocnej premennej
            stvorcek_x += 1

        #zmena pomocnych premennych
        stvorcek_x = 0
        stvorcek_y += 50

def mapa(): #funkcia na vykreslenie mapy pristavu
    x = 0
    y = 0
    
    for riadok in subor: #cyklus pre riadky v subore
        riadocek = riadok.split()

        for slovo in riadocek: #cyklus pre slova v riadku
            #podmienka na vykreslenie plochy na mape
            if slovo == "0":
                canvas.create_rectangle(x,y,x+50,y+50,fill="blue",outline="")
            else:
                canvas.create_rectangle(x,y,x+50,y+50,fill="grey",outline="")

            #zmena pomocnej premennej
            x += 50

        #zmena pomocnych premennych
        y += 50
        x = 0

def spawn(): #funkcia na vykreslenie lodiciek
    #zadeklarovanie globalnej premennej
    global pocitadielko

    #zadeklarovanie lokalnych premennych
    sirka1 = sirky[pocitadielko]
    vyska1 = vysky[pocitadielko]

    #vykreslenie lodicky
    canvas.create_rectangle(sirka1,vyska1,sirka1+150,vyska1+50,fill="yellow")

    #zmena pomocnej premennej
    pocitadielko += 1

    #podmienka na vypisanie oznamu o plnom pristave
    if pocitadielko == len(sirky):
        canvas.create_text(250,150,text="PRÍSTAV JE PLNÝ",font="Arial 20 bold")

#vykonanie funkcii       
zistenie()
mapa()

#vykreslenie tlacidla
tlacitko = tkinter.Button(text='Pridaj lodičku',command=spawn)
tlacitko.pack()

#zatvorenie suborov
subor.close()
subor1.close()


