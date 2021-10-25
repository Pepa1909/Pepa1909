x=7
while True:
    y = int(input("zadej číslo: "))
    if y > x:
        print("moc velké")
    elif y < x:
        print("moc malé")
    else:
        print("správně :)")
        break
print("konec")

