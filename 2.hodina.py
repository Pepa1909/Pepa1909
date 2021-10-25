alpha_deg = int(input("kolik stupňů? "))
if alpha_deg > 360 or alpha_deg < 0:
    print("stupně musí v intervalu <0, 360>")
    quit()
alpha_min = int(input("kolik minut? "))
if alpha_min >= 60 or alpha_min < 0:
    print("minuty musí být v inervalu <0, 60)")
    quit()
alpha_sec = float(input("kolik vteřin? "))
if alpha_sec >= 60 or alpha_sec < 0:
    print("sekundy musí být v inervalu <0, 60)")
    quit()
dec_deg = int(alpha_deg)
dec_min = alpha_min / 60
dec_sec = alpha_sec /3600
print(dec_deg+dec_min+dec_sec)