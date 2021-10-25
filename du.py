from turtle import *
print("""
Dobrý den, 
budete hrát piškvorky v poli 3x3. Musíte sledovat jak hrací tabulku, tak dotatečné informace v terminálu.
Během hry může kdykoliv napsat quit a tím hru ukončit
Rozmístění políček je následující:
7  8  9
4  5  6
1  2  3
""")
# hrac_1 = input("Jméno hráče 1: ")
print("Vy budete hrát s kolečky.")
# hrac_2 = input("Jméno hráče 2: ")
print("Váš tvar jsou křížky.")
# input("pro pokračování stiskněte klávesu Enter...")
speed(0)
up()
setpos(-250,-150)
down()
hrana=100
for _ in range (3):
    for _ in range(3):
        for _ in range(4):
            forward(hrana)
            left(90)
        forward(hrana)
    left(180)
    forward(hrana*3)
    right(90)
    forward(hrana)
    right(90)
# tah_1 = int(input(f"{hrac_1}, vyberte si políčko: "))
speed(6)
up()
for kolo in range(1):
    tah = (input("vyber policko (čísla 1-9): "))
    if tah == "1":
        setpos(-200, -140)
    elif tah == "2":
        setpos(-100,-140)
    elif tah == "3":
        setpos(0,-140)         
    elif tah == "4":
        setpos(-200, -40)
    elif tah == "5":
        setpos(-100,-40)
    elif tah == "6":
        setpos(0,-40)         
    elif tah == "7":
        setpos(-200, 60)
    elif tah == "8":
        setpos(-100, 60)     
    elif tah == "9":
        setpos(0,60)
    elif tah == "quit":
        quit()
    else:
         tah = input("zkus to znovu: ")
    down()
    circle(40)
    tah = (input("vyber policko (čísla 1-9): "))
    up()
    if tah == "1":
        setpos(-240, -140)
    elif tah == "2":
        setpos(-140,-140)
    elif tah == "3":
        setpos(-40,-140)
    elif tah == "4":
        setpos(-240, -40)
    elif tah == "5":
        setpos(-140,-40)
    elif tah == "6":
        setpos(-40,-40)
    elif tah == "7":
        setpos(-240, 60)
    elif tah == "8":
        setpos(-140, 60)
    elif tah == "9":
        setpos(-40,60)
    elif tah == "quit":
        quit()
    else:
         tah = input("zkus to znovu: ")
    down()
    left(45)
    forward(120)
    left(180)
    forward(60)
    left(90)
    forward(60)
    left(180)
    forward(120)

exitonclick()
    