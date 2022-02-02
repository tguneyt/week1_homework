# WEEK-1 Beden Kitle Endeksi Hesaplama
# Tayyip Güney

print("\nBEDEN KİTLE İNDEKSİ HESAPLAMA")
while True:
    try:
        kilo=float(input("\nLütfen Kilonuzu Girin (kg) : "))
        boy=float(input("Lüften Boyunuzu Girin (cm) : "))
        break
    except:
        print("\n!!! Hatalı giriş yaptınız...!!!")
        continue
        
sonuc= kilo/((boy/100)**2)
max_kilo=int(25*((boy/100)**2))

if sonuc <25:
    print("\nBKI =",sonuc,"\n\n*** Sonuç : NORMAL ***\n")
elif 25<=sonuc<30:
    print("\nBKI =",sonuc,"\n\n*** Sonuç : FAZLA KİLOLU ***\n\nBKI normal olması için "+ 
          "kilonuz\n"+str(max_kilo)+" kg olmalıdır.\n") 
elif 30<=sonuc<40:
    print("\nBKI =",sonuc,"\n\n*** Sonuç : OBEZ ***\n\nBKI normal olması için "+ 
          "kilonuz\n"+str(max_kilo)+" kg olmalıdır.\n") 
else:
    print("\nBKI =",sonuc,"\n\n*** Sonuç : AŞIRI ŞİŞMAN ***\n\nBKI normal olması için "+ 
          "kilonuz\n"+str(max_kilo)+" kg olmalıdır.\n")   