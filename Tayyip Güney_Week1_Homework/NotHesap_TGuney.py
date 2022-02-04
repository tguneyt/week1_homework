"""
Tayyip GÜNEY - 02.02.2022

Lesson Success Calculator

Name, Surname, Student Number, 4 course names, Midterm and Final grades 
of these courses will be requested from the user. 
The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average. 
If the average is less than 50, “FAILED” will be displayed on the screen, 
and if 50 and above, “PASSED” will be displayed on the screen. 
This printing process will be done in 4 lessons and the lessons will be printed one after the other.
"""

print("YILSONU BAŞARISI HESAPLAMA\n")
kullanici_ad = input("İsim Giriniz : ")
kullanici_soyad = input("\nSoyisim Giriniz : ")

while True:
    try:
        ogrenci_no= int(input("\nÖğrenci No Giriniz : "))
        break
    except:
        print("\n!!! Öğrenci Numarası Sadece Rakam İçerir !!!")
        continue
        
ders1= input("\nDersin Adını Giriniz : ")
while True:
    try:
        ders1_vize=float(input(f"\n{ders1} Dersinin VİZE Notunu Giriniz : "))
        ders1_final=float(input(f"\n{ders1} Dersinin FİNAL Notunu Giriniz : "))
        break
    except:
        print("!!! Hatalı Giriş Yaptınız !!!")
        continue
ders1_sonuc=(ders1_vize*4/10)+(ders1_final*6/10)

ders2= input("\nDersin Adını Giriniz : ")
while True:
    try:
        ders2_vize=float(input(f"\n{ders2} Dersinin VİZE Notunu Giriniz : "))
        ders2_final=float(input(f"\n{ders2} Dersinin FİNAL Notunu Giriniz : "))
        break
    except:
        print("!!! Hatalı Giriş Yaptınız !!!")
        continue
ders2_sonuc=(ders2_vize*4/10)+(ders2_final*6/10)

ders3= input("\nDersin Adını Giriniz : ")
while True:
    try: 
        ders3_vize=float(input(f"\n{ders3} Dersinin VİZE Notunu Giriniz : "))
        ders3_final=float(input(f"\n{ders3} Dersinin FİNAL Notunu Giriniz : "))
        break
    except:
        print("!!! Hatalı Giriş Yaptınız !!!")
        continue
ders3_sonuc=(ders3_vize*4/10)+(ders3_final*6/10)

ders4= input("\nDersin Adını Giriniz : ")
while True:
    try:
        ders4_vize=float(input(f"\n{ders4} Dersinin VİZE Notunu Giriniz : "))
        ders4_final=float(input(f"\n{ders4} Dersinin FİNAL Notunu Giriniz : "))
        break
    except:
        print("!!! Hatalı Giriş Yaptınız !!!")
        continue
ders4_sonuc=(ders4_vize*4/10)+(ders4_final*6/10)


yildiz=20*"*"
print(f"\nYILSONU NOT DURUMU\n{yildiz}")
if ders1_sonuc < 50:
    s_sonuc=f"\n{ders1} Dersi Yılsonu Notu = {ders1_sonuc}\nSonuç = KALDI\n"
else:
    s_sonuc=f"\n{ders1} Dersi Yılsonu Notu = {ders1_sonuc}\nSonuç = GEÇTİ\n"
    
if ders2_sonuc<50:
    s_sonuc=s_sonuc+f"\n{ders2} Dersi Yılsonu Notu = {ders2_sonuc}\nSonuç = KALDI\n"
else:
    s_sonuc=s_sonuc+f"\n{ders2} Dersi Yılsonu Notu = {ders2_sonuc}\nSonuç = GEÇTİ\n"

if ders3_sonuc<50:
    s_sonuc=s_sonuc+f"\n{ders3} Dersi Yılsonu Notu = {ders3_sonuc}\nSonuç = KALDI\n"
else:
    s_sonuc=s_sonuc+f"\n{ders3} Dersi Yılsonu Notu = {ders3_sonuc}\nSonuç = GEÇTİ\n"
   
if ders4_sonuc<50:
    s_sonuc=s_sonuc+f"\n{ders4} Dersi Yılsonu Notu = {ders4_sonuc}\nSonuç = KALDI\n"    
else:
    s_sonuc=s_sonuc+f"\n{ders4} Dersi Yılsonu Notu = {ders4_sonuc}\nSonuç = GEÇTİ\n"


print("\nÖğrenci Bilgileri :",ogrenci_no," - "+kullanici_ad+" "+kullanici_soyad+"\n"+s_sonuc)    
                 
