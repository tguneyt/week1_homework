# WEEK-1 Yılsonu Not Hesaplama
# Tayyip Güney

from re import T
import ssl

from pkg_resources import yield_lines


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
print(f"\nÖğrenci : {ogrenci_no} - {kullanici_ad} {kullanici_soyad}\n")       
for i in range(0,4):
    print(list[i])       
     
# while True:
#     try:
#         ogrenci_no= int(input("\nÖğrenci No Giriniz : "))
#         break
#     except:
#         print("\n!!! Öğrenci Numarası Sadece Rakam İçerir !!!")
#         continue
        
# ders1= input("\nDersin Adını Giriniz : ")
# while True:
#     try:
#         ders1_vize=float(input(f"\n{ders1} Dersinin VİZE Notunu Giriniz : "))
#         ders1_final=float(input(f"\n{ders1} Dersinin FİNAL Notunu Giriniz : "))
#         break
#     except:
#         print("!!! Hatalı Giriş Yaptınız !!!")
#         continue
# ders1_sonuc=(ders1_vize*4/10)+(ders1_final*6/10)

# ders2= input("\nDersin Adını Giriniz : ")
# while True:
#     try:
#         ders2_vize=float(input(f"\n{ders2} Dersinin VİZE Notunu Giriniz : "))
#         ders2_final=float(input(f"\n{ders2} Dersinin FİNAL Notunu Giriniz : "))
#         break
#     except:
#         print("!!! Hatalı Giriş Yaptınız !!!")
#         continue
# ders2_sonuc=(ders2_vize*4/10)+(ders2_final*6/10)

# ders3= input("\nDersin Adını Giriniz : ")
# while True:
#     try: 
#         ders3_vize=float(input(f"\n{ders3} Dersinin VİZE Notunu Giriniz : "))
#         ders3_final=float(input(f"\n{ders3} Dersinin FİNAL Notunu Giriniz : "))
#         break
#     except:
#         print("!!! Hatalı Giriş Yaptınız !!!")
#         continue
# ders3_sonuc=(ders3_vize*4/10)+(ders3_final*6/10)

# ders4= input("\nDersin Adını Giriniz : ")
# while True:
#     try:
#         ders4_vize=float(input(f"\n{ders4} Dersinin VİZE Notunu Giriniz : "))
#         ders4_final=float(input(f"\n{ders4} Dersinin FİNAL Notunu Giriniz : "))
#         break
#     except:
#         print("!!! Hatalı Giriş Yaptınız !!!")
#         continue
# ders4_sonuc=(ders4_vize*4/10)+(ders4_final*6/10)

# yildiz=20*"*"
# print(f"\nYILSONU NOT DURUMU\n{yildiz}")
# if ders1_sonuc < 50:
#     s_sonuc=f"\n{ders1} Dersi Yılsonu Notu = {ders1_sonuc}\nSonuç = KALDI\n"
# else:
#     s_sonuc=f"\n{ders1} Dersi Yılsonu Notu = {ders1_sonuc}\nSonuç = GEÇTİ\n"
    
# if ders2_sonuc<50:
#     s_sonuc=s_sonuc+f"\n{ders2} Dersi Yılsonu Notu = {ders2_sonuc}\nSonuç = KALDI\n"
# else:
#     s_sonuc=s_sonuc+f"\n{ders2} Dersi Yılsonu Notu = {ders2_sonuc}\nSonuç = GEÇTİ\n"

# if ders3_sonuc<50:
#     s_sonuc=s_sonuc+f"\n{ders3} Dersi Yılsonu Notu = {ders3_sonuc}\nSonuç = KALDI\n"
# else:
#     s_sonuc=s_sonuc+f"\n{ders3} Dersi Yılsonu Notu = {ders3_sonuc}\nSonuç = GEÇTİ\n"
   
# if ders4_sonuc<50:
#     s_sonuc=s_sonuc+f"\n{ders4} Dersi Yılsonu Notu = {ders4_sonuc}\nSonuç = KALDI\n"    
# else:
#     s_sonuc=s_sonuc+f"\n{ders4} Dersi Yılsonu Notu = {ders4_sonuc}\nSonuç = GEÇTİ\n"

# print("\nÖğrenci Bilgileri :",ogrenci_no," - "+kullanici_ad+" "+kullanici_soyad+"\n"+s_sonuc)    
                 