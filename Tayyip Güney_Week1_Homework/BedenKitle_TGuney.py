"""
Tayyip GÜNEY - 02.02.2022

Program : Body Mass Index

The program takes the name, surname, weight and height. And it gives Body Mass Index and Classify of BMI.
Take the weight and height from the user and write a warning as Underweight 
if the index<25; normal 
25=< the index < 30; overweight
30=< the index <40 obese
>40, extreme fat
"""

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
