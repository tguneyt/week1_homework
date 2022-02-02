# WEEK-1 Taş-Kağıt-Makas Oyunu
# Tayyip Güney

from random import randint

print("""  
Taş-Kağıt-Makas Oyununa 
      HOŞGELDİNİZ
       
10 skoruna ilk ulaşan kazanır.    
""")
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
   
if mod ==1: #Bilgisayara Karşı Oyna
    
    oyuncu_1 = input("Lütfen isminizi giriniz: ")
    oyuncu_2="Bilgisayar"

    liste = ["Taş", "Kağıt", "Makas"]

    r2=randint(0,2) #random sayı 0,1,2
    say_1=0
    say_2=0
    s1 = "\nBu turu *** "+oyuncu_1+" *** KAZANDI\n"
    s2 = "\nBu turu *** "+oyuncu_2+" *** KAZANDI\n"
    tur=0

    while say_1!=10 and say_2!=10: #herhangi biri 10 olursa oyun biter
        
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
        r1=secim_1-1 # liste index'i 0,1,2 olduğu için r1=sec-1
        r2=randint(0,2)
        
        if (r1==0 and r2==1):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s2) 
            say_2+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==0 and r2==2):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s1)  
            say_1+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==1 and r2==0):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s1) 
            say_1+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==1 and r2==2):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s2) 
            say_2+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==2 and r2==0):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s2) 
            say_2+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==2 and r2==1):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s1) 
            say_1+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
                    
        else:
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+"\n-BERABERE-\n") 
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
        
    yildiz=50*"*"  
    print(yildiz+f"\nOYUN {tur} TURDA SONA ERDİ\n\nGENEL SKOR : {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}")
    if say_1==10:
        print("\n"+yildiz+"\n\nOYUNUN GALİBİ : "+oyuncu_1+"\n\n"+yildiz)
    else:
        print("\n"+yildiz+"\n\nOYUNUN GALİBİ : "+oyuncu_2+"\n\n"+yildiz)

################################################################################################################################

else: #İki kişilik Oyun
   
    oyuncu_1 = input("1. Oyuncunun isminizi giriniz: ")
    oyuncu_2 = input("2. Oyuncunun isminizi giriniz: ")

    liste = ["Taş", "Kağıt", "Makas"]

    #r2=randint(0,2) #random sayı 0,1,2
    say_1=0
    say_2=0
    s1 = "\nBu turu *** "+oyuncu_1+" *** KAZANDI\n"
    s2 = "\nBu turu *** "+oyuncu_2+" *** KAZANDI\n"
    tur=0

    while say_1!=10 and say_2!=10: #herhangi biri 10 olursa oyun biter
        
        try: #listedeki sayıyı girerse devam
            secim_1=int(input(f"""
{oyuncu_1} - Seçtiğiniz Eşyanın Sıra Numarasını Giriniz...

1- Taş
2- Kağıt
3- Makas
"""))
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
            except: #string değer girerse tekrar sayı iste
                print(f"\n!!!{oyuncu_1} - Lütfen rakam giriniz...!!!")
                continue
###########oyuncu-2
        try: #listedeki sayıyı girerse devam
            secim_2=int(input(f"""
{oyuncu_2} - Seçtiğiniz Eşyanın Sıra Numarasını Giriniz...

1- Taş
2- Kağıt
3- Makas
"""))
        except: #string değer girerse tekrar sayı iste
            print(f"\n!!! {oyuncu_1} - Lütfen rakam giriniz...!!!")
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
            except: #string değer girerse tekrar sayı iste
                print(f"\n!!! {oyuncu_2} - Lütfen rakam giriniz...!!!")
                continue            
        tur+=1    
        r1=secim_1-1 # liste index'i 0,1,2 olduğu için r1=sec-1
        r2=secim_2-1
        
        if (r1==0 and r2==1):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s2) 
            say_2+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==0 and r2==2):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s1)  
            say_1+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==1 and r2==0):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s1) 
            say_1+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==1 and r2==2):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s2) 
            say_2+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==2 and r2==0):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s2) 
            say_2+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
            
        elif (r1==2 and r2==1):
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+s1) 
            say_1+=1
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
                    
        else:
            print("\n"+oyuncu_1," = ",liste[r1]+"\n"+oyuncu_2," = ",liste[r2]+"\n"+"\n-BERABERE-\n") 
            print(f"{tur}. Tur Skoru = {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}\n")
            continue
        
    yildiz=50*"*"  
    print(yildiz+f"\nOYUN {tur} TURDA SONA ERDİ\n\nGENEL SKOR : {oyuncu_1}  {say_1} : {say_2}  {oyuncu_2}")
    if say_1==10:
        print("\n"+yildiz+"\n\nOYUNUN GALİBİ : "+oyuncu_1+"\n\n"+yildiz)
    else:
        print("\n"+yildiz+"\n\nOYUNUN GALİBİ : "+oyuncu_2+"\n\n"+yildiz)