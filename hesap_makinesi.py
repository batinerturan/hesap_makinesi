## Author : @M.Batın Erturan
## Author : @H. Ali Özkan
## 06.12.2023

def toplama(birinci_sayı, ikinci_sayı):
    sonuç = birinci_sayı + ikinci_sayı
    return sonuç

def çıkarma(birinci_sayı, ikinci_sayı):
    sonuç = birinci_sayı - ikinci_sayı
    return sonuç

def çarpma(birinci_sayı, ikinci_sayı):
    sonuç = birinci_sayı * ikinci_sayı
    return sonuç

def bölme(birinci_sayı, ikinci_sayı):
    if ikinci_sayı == 0: #4/0
        print("Herhangi bir sayı 0'a bölünemez lütfen başka sayı giriniz!")
        return "İşlem Başarısız"
    else:
        sonuç = birinci_sayı // ikinci_sayı
        return sonuç


# Üslü sayılar yazılacak

def üslü(birinci_sayı, ikinci_sayı):
    sonuç = birinci_sayı ** ikinci_sayı
    return sonuç

# Modulus işlemi yazılacak
def modulus(birinci_sayı, ikinci_sayı):
    sonuç = birinci_sayı % ikinci_sayı
    return sonuç

#1.km 2.hm 3.Dam 4.m 5.dm 6.cm 7.mm

#1-> km   
#2-> hm
#3-> Dam
#4-> m
#5-> dm
#6-> cm
#7-> mm


# 1km -> 1km 
# 1km -> 1000 m
# 1km -> 1_000_000 mm
# 1m ->  1000 mm

# 1m -> 0,001

# 55km kaç m'dir.
#  dönüştürülecek = km
#  dönüşecek = m
#  sayı = 55

# fark = m(4) - km(1)  = 3
# 55000
            # 4         1             1
def uzunluk(dönüşecek,dönüştürülecek,sayı):
    # -3 =        1        -   4 
    fark = dönüştürülecek - dönüşecek

    if fark == 0:
        return sayı
    
    elif fark < 0:
        fark =  fark*-1 # 3
        kat = '0'*fark #'000'
        return sayı / int('1' + kat) # '1000'
               # 1  % 1000
    else: 
        kat = '0'*fark
        return sayı * int('1' + kat)
    
    
# 1e-06 = bilimsel gösterim
# 0,000001

#12e-11
#0,000000000012

#12e+11
#1200000000000

#press = baskı

#pass = pas geçmek
    """
    if dönüşecek == 'km':
        match dönüştürülecek:
            case 'hm':
                sonuç = sayı *10
                return sonuç
            case 'Dam':
                sonuç = sayı *100
                return sonuç
            case 'm':
                sonuç = sayı *1000
                return sonuç
            case 'dm':
                sonuç = sayı *10000
                return sonuç
            case 'cm':
                sonuç = sayı *100000
                return sonuç
            case 'mm':
                sonuç = sayı *1000000
                return sonuç
            case _:
                return -1

    elif dönüşecek == 'hm':
        match dönüştürülecek:
            case 'Dam':
                sonuç = sayı *100
                return sonuç
            case 'm':
                sonuç = sayı *1000
                return sonuç
            case 'dm':
                sonuç = sayı *10000
                return sonuç
            case 'cm':
                sonuç = sayı *100000
                return sonuç
            case 'mm':
                sonuç = sayı *1000000
                return sonuç
            case 'km':
                sonuç = sayı %10
                return sonuç
            case _:
                return -1
    """

#1kg = 1000g
def ağırlık(dönüşecek,dönüştürülecek,sayı):
    fark = dönüştürülecek - dönüşecek
    if fark ==  0:
        return sayı

    elif fark < 0:
        fark = fark*-1
        kat = '0'*fark
        return sayı / int('1' + kat)

    else:
        kat = '0'*fark
        return sayı * int('1'+ kat)

#1.km3 2.hm3 3.Dam3 4.m3 5.dm3 6.cm3 7.mm3
def hacim(dönüşecek,dönüştürülecek,sayı):
    fark = dönüştürülecek - dönüşecek

    if fark ==  0:
        return sayı

    elif fark < 0:
        fark = fark*-1
        kat = '000'*fark
        return sayı / int('1' + kat)

    else:
        kat = '000'*fark
        return sayı * int('1'+ kat)


#1km2 =  1_000_000 m2

def alan(dönüşecek,dönüştürülecek,sayı):
    fark = dönüştürülecek -dönüşecek

    if fark == 0:
        return sayı

    elif fark < 0:
        fark =fark*-1
        kat = '00'*fark
        return sayı / int('1' + kat)
    
    else:
        kat = '00'*fark
        return sayı * int('1' + kat)


def matematik_sonuç (fonksiyon):
    print("----------------------")
    print("Sonuç : ", str(fonksiyon(birinci_sayı,ikinci_sayı)))
    print()
    print("----------------------")
   
         



# Dönüşümler ekelenecek (1 km = 1000m, 1 kg = 1000g, 1L = 1000ml )

# 1) Matematiksel Hesaplama
# 2) Dönüşüm
# 3) Çıkış Yap

#1
#1.Toplama
#2.Çıkarma
#3.Çarpma
#4.Bölme
#5.Üs Alma
#6.Modulus
#7.Geriye Git

#2
#1.Uzunluk
#2.Ağırlık
#3.Hacim
#4.Geriye Git


while True:
    print("1.Matematiksel İşlem\n2.Dönüşüm\n3.Çıkış Yap")
    işlem = int(input("\nLütfen bir işlem seçiniz : "))
    if işlem < 1:
        print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
        continue
    if işlem > 3:
        print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
        continue
    if işlem == 3:
        break
    else:
        if işlem == 1:
            while True: 
                print("1.Toplama\n2.Çıkarma\n3.Çarpma\n4.Bölme\n5.Üssünü Al\n6.Modulus\n7.Geriye Git")
                işlem = int(input("\nLütfen bir işlem seçiniz : "))
                if işlem < 1:
                    print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
                    continue
                if işlem > 7:
                    print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
                    continue
                if işlem == 7:
                    break
                else:
                    
                    birinci_sayı = int(input("Birinci sayıyı giriniz: "))
                    ikinci_sayı = int(input("İkinci sayıyı giriniz : "))
                    
                    # 1 Toplama
                    if işlem == 1:
                        matematik_sonuç(toplama)
                    # 2 Çıkarma
                    elif işlem == 2:
                       matematik_sonuç(çıkarma)
                    # 3 Çarpma
                    elif işlem == 3:
                        matematik_sonuç(çarpma)
                    # 4 Bölme
                    elif işlem == 4:
                        matematik_sonuç(bölme)
                    elif işlem == 5:
                        matematik_sonuç(üslü)
                    elif işlem == 6:
                        matematik_sonuç(modulus)
                    else:
                        print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
                        continue
        if işlem == 2:
            while True:
                print("1.Uzunluk\n2.Ağırlık\n3.Hacim\n4.Alan\n5.Geriye Git")
                işlem = int(input("\nLütfen bir işlem seçiniz : "))
               
                if işlem < 1:
                    print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
                    continue
                if işlem > 5:
                    print("Hatalı seçim yaptınız.Lütfen tekrar seçim yapınız\n")
                    continue
                if işlem == 5:
                    break
                else:
                    if işlem == 1:
                        birimler = ["km","hm","Dam","m","dm","cm","mm"]
                        print("1.km\n2.hm\n3.Dam\n4.m\n5.dm\n6.cm\n7.mm")
                        dönüşecek_birim = int(input("\nLütfen dönüşecek birimi seçiniz:"))
                        dönüşecek_sayı = int(input("\nLütfen dönüşecek sayıyı yazın: "))
                        print("1.km\n2.hm\n3.Dam\n4.m\n5.dm\n6.cm\n7.mm")
                        dönüştürülecek_birim = int(input("\nLütfen dönüştürülecek birimi seçiniz:"))
                        print("----------------------")
                        print("Sonuç :  ", str(uzunluk(dönüşecek_birim,dönüştürülecek_birim,dönüşecek_sayı)),birimler[dönüştürülecek_birim-1])
                        print()
                        print("----------------------")
                    if işlem == 2:
                        birimler = ["kg","hg","Dag","g","dg","cg","mg"]
                        print("1.kg\n2.hg\n3.Dag\n4.g\n5.dg\n6.cg\n7.mg")
                        dönüşecek_birim = int(input("\nLütfen dönüşecek birimi seçiniz:"))
                        dönüşecek_sayı = int(input("\nLütfen dönüşecek sayıyı yazın: "))
                        print("1.kg\n2.hg\n3.Dag\n4.g\n5.dg\n6.cg\n7.mg")
                        dönüştürülecek_birim = int(input("\nLütfen dönüştürülecek birimi seçiniz:"))
                        print("----------------------")
                        print("Sonuç :  ", str(ağırlık(dönüşecek_birim,dönüştürülecek_birim,dönüşecek_sayı)),birimler[dönüştürülecek_birim-1])
                        print()
                        print("----------------------")
                    if işlem == 3:
                        birimler = ["km3","hm3","Dam3","m3","dm3","cm3","mm3"]
                        print("1.km3\n2.hm3\n3.Dam3\n4.m3\n5.dm3\n6.cm3\n7.mm3")
                        dönüşecek_birim = int(input("\nLütfen dönüşecek birimi seçiniz:"))
                        dönüşecek_sayı = int(input("\nLütfen dönüşecek sayıyı yazın: "))
                        print("1.km3\n2.hm3\n3.Dam3\n4.m3\n5.dm3\n6.cm3\n7.mm3")
                        dönüştürülecek_birim = int(input("\nLütfen dönüştürülecek birimi seçiniz:"))
                        print("----------------------")
                        print("Sonuç :  ", str(hacim(dönüşecek_birim,dönüştürülecek_birim,dönüşecek_sayı)),birimler[dönüştürülecek_birim-1])
                        print()
                        print("----------------------")
                    if işlem == 4:
                        birimler = ["km2","hm2","Dam2","m2","dm2","cm2","mm2"]
                        print("1.km2\n2.hm2\n3.Dam2\n4.m2\n5.dm2\n6.cm2\n7.mm2")
                        dönüşecek_birim = int(input("\nLütfen dönüşecek birimi seçiniz:"))
                        dönüşecek_sayı = int(input("\nLütfen dönüşecek sayıyı yazın: "))
                        print("1.km2\n2.hm2\n3.Dam2\n4.m2\n5.dm2\n6.cm2\n7.mm2")
                        dönüştürülecek_birim = int(input("\nLütfen dönüştürülecek birimi seçiniz:"))
                        print("----------------------")
                        print("Sonuç :  ", str(alan(dönüşecek_birim,dönüştürülecek_birim,dönüşecek_sayı)),birimler[dönüştürülecek_birim-1])
                        print()
                        print("----------------------")
#new-line = yeni satır 
#if = eğer
#elif = else if =  değilse eğer 
#else = değilse
#1.000.000.000
#1.000.000.000
#1. 1   2   3