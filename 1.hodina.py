import math
a = int(input("napiš koeficient x^2: "))
b = int(input("napiš koeficient u x: "))
c = int(input("napiš koeficient u 1: "))
diskriminant = b**2-4*a*c
if diskriminant > 0:
    print("kořeny jsou 2:", (-b+math.sqrt(diskriminant))/2*a, "a", (-b-math.sqrt(diskriminant))/2*a)
elif diskriminant == 0:
    print("dvojnásobný kořen je", -b/2*a)
else:
    print("diskriminant je menší než 0, řešení nejsou")