# WEEK-1 Taş-Kağıt-Makas Oyunu
# Tayyip Güney

from random import randint
print("""  
Taş-Kağıt-Makas Oyununa 
      HOŞGELDİNİZ       
""")

liste = ["Taş", "Kağıt", "Makas"]
say_1=0
say_2=0
tur=0
################## Mod Seçimi ##################
while True: #String Değer Giremesin 
    try:
        mod=int(input("1-Bilgisayara Karşı\n2-İki Oyunculu\n"))
        break
    except:
        print("\n!!! Lütfen rakam giriniz...!!!")
        continue
        
while (mod!=1 and mod!=2): # 1 veya 2 seçilmeli
            try:
                mod=int(input(
    """
!!! HATALI SEÇİM !!!. Lütfen tekrar giriniz.
    
1-Bilgisayara Karşı
2-İki Oyunculu
"""))
            except: #string değer girerse tekrar sayı iste
                print("\n!!! Lütfen rakam giriniz...!!!")
                continue
################## Mod Seçimi ##################

if mod ==1: #Bilgisayara Karşı Oyna
    oyuncu_1 = input("Lütfen isminizi giriniz: ")
    oyuncu_2="Bilgisayar"   
else:    # İKİ KİŞİLİK OYUN
    oyuncu_1 = input("1. Oyuncunun isminizi giriniz: ")
    oyuncu_2 = input("2. Oyuncunun isminizi giriniz: ")  
    
s1 = "\nBu turu *** "+oyuncu_1+" *** KAZANDI\n"
s2 = "\nBu turu *** "+oyuncu_2+" *** KAZANDI\n" 
  
while say_1!=10 and say_2!=10: #10 olan kazanır(def)
#while tur<10: #10 turda oyun biter(değiştirilebilir)    
    if mod==1:    #Bilgisayara Karşı Oyna
        try: #listedeki sayıyı girerse devam
            secim_1=int(input("""
Seçtiğiniz Eşyanın Sıra Numarasını Giriniz...
1- Taş
2- Kağıt
3- Makas
"""))
        except: #string değer girerse tekrar sayı iste
            print("\n!!! Lütfen rakam giriniz...!!!")
            continue    
        
        while (secim_1!=1 and secim_1!=2 and secim_1!=3): #Listedekiler dışında yanlış seçim yapılmasın
            try:
                secim_1=int(input(
"""
!!! HATALI SEÇİM !!!. Lütfen tekrar giriniz.
1- Taş
2- Kağıt
3- Makas
"""))
            except: #string değer girerse tekrar sayı iste
                print("\n!!! Lütfen rakam giriniz...!!!")
                continue
            
        tur+=1    
        r1=secim_1-1 # liste index'i 0,1,2 olduğu için -1
        r2=randint(0,2) #Bilgisayar için random sayı üret
############### İKİ KİŞİLİK OYUN         
    else:   # İKİ KİŞİLİK OYUN
        
        x=1
        while True: # Oyuncu-1 Seçim
            if x==1: # hatalı seçimden dönüşte tekrar buraya girmesin
                try: 
                    secim_1=int(input(f"""
{oyuncu_1} - Seçtiğiniz Eşyanın Sıra Numarasını Giriniz...
1- Taş
2- Kağıt
3- Makas
"""))
                    if(secim_1==1 or secim_1==2 or secim_1==3):
                        x=2 # Oyuncu-2 döngüsüne girmeli
                        break
                except: #string değer girerse tekrar sayı iste
                    print(f"\n!!! {oyuncu_1} - Lütfen rakam giriniz...!!!")
                    continue    
            
                while (secim_1!=1 and secim_1!=2 and secim_1!=3): #Listedekiler dışında yanlış seçim yapılmasın
                    try:
                        secim_1=int(input(
f"""
!!! {oyuncu_1} - HATALI SEÇİM !!!. Lütfen tekrar giriniz.
1- Taş
2- Kağıt
3- Makas
"""))
                        if(secim_1==1 or secim_1==2 or secim_1==3):
                            x=2 # dönüşte tekrar döngüye girmesin
                            break
                    except: #string değer girerse tekrar sayı iste
                        print(f"\n!!!Lütfen rakam giriniz...!!!")
                        continue
            else: # x != 1
                break            

        while True:  # Oyuncu-2 Seçim
            if x == 2: # Hatalı seçimden dönüşte tekrar girmesin
                try: #listedeki sayıyı girerse devam
                    secim_2=int(input(f"""
{oyuncu_2} - Seçtiğiniz Eşyanın Sıra Numarasını Giriniz...
1- Taş
2- Kağıt
3- Makas
"""))
                    if secim_2==1 or secim_2==2 or secim_2==3:
                        x==1 # oyuncu-1 döngüsüne girmeli
                        break
                except: #string değer girerse tekrar sayı iste
                    print(f"\n!!! {oyuncu_2} - Lütfen rakam giriniz...!!!")
                    continue  
                
                while (secim_2!=1 and secim_2!=2 and secim_2!=3): #Listedekiler dışında yanlış seçim yapılmasın
                    try:
                        secim_2=int(input(
f"""
!!! {oyuncu_2} - HATALI SEÇİM !!!. Lütfen tekrar giriniz.
1- Taş
2- Kağıt
3- Makas
"""))
                        if secim_2==1 or secim_2==2 or secim_2==3:
                            x=1 # dönüşte tekrar döngüye girmesin
                            break
                    except: #string değer girerse tekrar sayı iste
                        print(f"\n!!! {oyuncu_2} - Lütfen rakam giriniz...!!!")
                        continue  
            else:
                break

        tur+=1    
        r1=secim_1-1 # liste index'i 0,1,2 olduğu için r1=sec-1
        r2=secim_2-1
        
########## SONUÇLAR  
    cizgi=50*"_"
    yildiz=50*"*" 
    if (r1==0 and r2==1): #continue ile döngüye devam ettiği için skoru dışarıda tanımlama
        say_2+=1
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+f"\n{cizgi}\n{s2}"+
              f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}") 
        continue
    elif (r1==0 and r2==2):
        say_1+=1
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+f"\n{cizgi}\n{s1}"+
              f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}")  
        continue
    elif (r1==1 and r2==0):
        say_1+=1
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+
              f"\n{cizgi}\n{s1}"+f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}") 
        continue     
    elif (r1==1 and r2==2):
        say_2+=1
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+
              f"\n{cizgi}\n{s2}"+f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}") 
        continue       
    elif (r1==2 and r2==0):
        say_2+=1
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+
              f"\n{cizgi}\n{s2}"+f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}") 
        continue      
    elif (r1==2 and r2==1):
        say_1+=1
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+
              f"\n{cizgi}\n{s1}"+f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}") 
        continue 
    else:
        print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+
              f"\n{cizgi}\n\n    -BERABERE-\n"+f"\n{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n{cizgi}") 
        continue  
print(yildiz+f"\nOYUN {tur} TURDA SONA ERDİ\n\nGENEL SKOR : {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}")
if say_1>say_2:
    print("\n"+yildiz+"\n\nOYUNUN GALİBİ : "+oyuncu_1+"\n\n"+yildiz)
elif say_2>say_1:
    print("\n"+yildiz+"\n\nOYUNUN GALİBİ : "+oyuncu_2+"\n\n"+yildiz)
else:
    print("\n"+yildiz+"\n\nOYUN BERABERE BİTTİ\n\n"+yildiz)
