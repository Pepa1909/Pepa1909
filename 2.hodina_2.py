dec = float(input("zadej úhel v decimálním tvaru: "))
if dec > 360 or dec < 0:
    print("zadej úhel v intervalu <0, 360>")
    quit()
deg = int(dec)
min_float = (dec-deg)*60
min = int(min_float)
sec = (min_float-min)*60
vysl = (deg,min,sec)
print(vysl)
#print(f"""výsledek je {deg}°{min}´{sec}"
#""")