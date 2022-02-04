"""
Tayyip GÜNEY - 04.02.2022

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
ogrenci_no = input("\nÖğrenci No Giriniz: ")
list = ["","","",""]
for i in range(1,5):
    ders = input(f"\n{i}. Dersin Adını Girin : ")
    while True:
        try:
            vize = float(input(f"{i}. Dersin Vize Notunu Girin : "))
            final = float(input(f"{i}. Dersin Final Notunu Girin : "))
            break
        except: 
            print("\n!!! Hatalı Giriş Yaptınız !!!\n")
            continue
    ort = (vize*4/10)+(final*6/10)
    y=30*"_"
    if ort<50:
        s_son=f"{y}\n{ders} Dersi Not Ortalaması = {ort}\n\nSonuç = KALDI"
        #print(s_son)
        list[i-1]=str(s_son)
    else:
        s_son=f"{y}\n{ders} Dersi Not Ortalaması = {ort}\n\nSonuç = GEÇTİ"
        #print(s_son)
        list[i-1]=str(s_son)
print(f"\nÖğrenci Bilgileri : {ogrenci_no} - {kullanici_ad} {kullanici_soyad}\n")       
for i in range(0,4):
    print(list[i])       
