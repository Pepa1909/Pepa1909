from random import *
x= randrange(101)
y = int(input("hádej číslo od 0 do 100: "))
while True:
    if y > x:
        print("hledan číslo je menší")
    elif y < x:
        print("hledané číslo je větší")
    else:
        print("správně :)")
        break
    y=int(input("zkus to znovu: "))
print("konec")