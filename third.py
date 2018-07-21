import os

def start():
    os.system("clear")
    print("Terzi Programına Hoşgeldiniz!")
    print("Bu gün ne yapmak istiyorsunuz?\n")
    print("1 - Ölüçü almak istiyorum")
    print("\nq - Çıkış")
    answer = input("--> ")

    if answer is "1":       # 1- ölcü al
        os.system("clear")
        take_dimentions()

    elif answer is "q":     # e- çıkış
        os.system("clear")
        quit()

def take_dimentions():

    print("Neyin Ölçüsünü almak istersiniz?\n")
    print("1 - Gömlek")
    print("\ng - Geri git")
    print("q - Çıkış")

    answer = input("--> ")

    if answer is "1":       # 1 - jeket
        os.system("clear")
        gomlek()

    elif answer is "q":     # e - çıkış
        os.system("clear")
        quit()

    elif answer is "g":     # g - geri
        os.system("clear")
        start()


#      _     _       _         _ _
#  ___| |__ | | ___ | |_ ___  (_) |_ ___ _ __ ___  ___
# / __| '_ \| |/ _ \| __/ _ \ | | __/ _ \ '_ ` _ \/ __|
#| (__| | | | | (_) | ||  __/ | | ||  __/ | | | | \__ \
# \___|_| |_|_|\___/ \__\___| |_|\__\___|_| |_| |_|___/
#


def gomlek():


    os.system("clear")
    print("Lütfen modelin ölçülerini alınız.")
    print("Ölçüleri girerken ondalıklı sayılarda nokra (.) kullanınız. harf kullanmayınız\n")

    # Ölçüler alınıyor

    print("\nBoyun Yarıçapı. Boyun Çevresini ölçün ve ikiye bölün"); SSH = float(input("СШ : "))

    print("\nBoyun Esneklik payının yarısı "); PRSH = float(input("ПРШ : "))

    print("\nGöğüs Yarıçapı"); CG = float(input("СГ : "))

    print("\nGöğüs Genişliği"); SHG = float(input("ШГ : "))

    print("\nGöğüs Çevresi Esneklik Payının yarısı"); PR = float(input("ПРГ : "))

    print("\nTrapez başlangıcından -> Meme ucuna kadar"); VG = float(input("ВГ : "))

    print("\nÖnden, Trapez başlangıcından -> Bele kadar DÜZ"); DPT = float(input("ДПТ : "))

    print("\nSırt Uzunluğu. Arkadan, 7. Omurdan -> Bele kadar"); DCT = float(input("ДСТ : "))

    print("\nGömlek uzunluğu"); DI = float(input("ДИ : "))

    print("\nArkadan, Omuz ucundan -> Belin ortasına kadar ÇAPRAZLAMA"); VPKS = float(input("ВПКС : "))

    print("\nSırt Genişliği"); SHS = float(input("ШС : "))

    print("\nTrapez başından -> Omuz ucuna kadar, Omuz genişliği"); DP = float(input("ДП : "))

    print("\nKol Uzunluğu, Omuz Ucundan -> Baş Parmağın ilk eklemine kadar"); DR = float(input("ДР : "))

    print("\nKoltuk altından, Üst Kol Çevresi"); OP = float(input("ОП : "))

    print("\nEsneklik Payını giriniz"); OP = float(input("ОП : "))

    # Gerekli Hesaplamalar yapılıyor

    # ?

    AG  = round((((DCT / 4) + ( CG / 2 ) / 4) + (PR / 4)), 1)
    GG1 = round(CG + (OP / 2),1) # burada eklenmesi gereken bir değer vardı if ile soracaktın

    # Arka Taraf

    GP  = round((SHS + OP/2),1)
    PP1 = round((DP/3 + OP/2),1) # gene +1 vardı opsiyonel if ile soracaktın
    AR  = round((SSH/3 + PRSH),1)
    RR1 = round((AR / 3),1)
    TP2 = round((VPKS + 2),1)
    R1P3= round((OP + 0.5),1)
    PP4 = round((PP1 / 2),1)
    PP5 = round((PP1 / 3),1)
    P1P6= round(((PP1 / 3) -1),1)

    # Ön Taraf

    P1G1 = round((SHG + (PR / 2) / 2),1)
    G1V  = round((VG),1)
    T1V  = round((DPT),1)
    V2P7 = round((DP),1)

    # Uzun Kol

    ON  = round((DR - 6.5),1)
    OV  = round((PP1 -2),1)
    VV1 = round(((PP1*3)/2),1)
    NN1 = round((PP1),1)

    # Kısa Kol

    OV  = round((PP1),1)
    VV1 = round(((OP + 10)/2),1)

    os.system("clear")
    print("Kalıp Değerleri")
    print("~~~~~~~~~~~~~~~\n")

    print("АГ   : {}".format(AG))
    print("ГГ1  : {}".format(GG1))

    print("\nArka Taraf")
    print("~~~~~~~~~~\n")

    print("ГП   : {}".format(GP  ))
    print("ПП1  : {}".format(PP1 ))
    print("АР   : {}".format(AR  ))
    print("РР1  : {}".format(RR1 ))
    print("ТП2  : {}".format(TP2 ))
    print("Р1П3 : {}".format(R1P3))
    print("ПП4  : {}".format(PP4 ))
    print("ПП5  : {}".format(PP5 ))
    print("П1П6 : {}".format(P1P6))

    print("\nÖn Taraf")
    print("~~~~~~~~\n")

    print("П1Г1 : {}".format(P1G1))
    print("Г1В  : {}".format(G1V ))
    print("Т1В  : {}".format(T1V ))
    print("В2П7 : {}".format(V2P7))

    print("\nUzun Kol")
    print("~~~~~~~~\n")

    print("ОН   : {}".format(ON))
    print("ОВ   : {}".format(OV))
    print("ВВ1  : {}".format(VV1))
    print("НН1  : {}".format(NN1))

    print("\nKısa Kol")
    print("~~~~~~~~\n")

    print("ОВ   : {}".format(OV))
    print("ВВ1  : {}".format(VV1))

start()
