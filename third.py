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

    # Ölçüler Alınıyor

    Сш =  float(input("Полуобхват шеи, Сш               : "))
    Сг =  float(input("Полуобхват груди, Сг             : "))
    Шг =  float(input("Ширина груди, Шг                 : "))
    Вг =  float(input("Высота груди, Вг                 : "))
    Дпт = float(input("Длина переда до линии талии, Дпт : "))
    Дст = float(input("Длина спины до линии талии, Дст  : "))
    Ди =  float(input("Длина изделия, Ди                : "))
    Впс = float(input("Высота плеча спины, Впс          : "))
    Шс =  float(input("Ширина спины, Шс                 : "))
    Дп =  float(input("Длина плеча, Дп                  : "))
    Др =  float(input("Длина рукава, Др                 : "))
    Оп =  float(input("Обхват плеча, Оп                 : "))
    Шп =  float(input("Şırina pleça, Шп                 : "))
    Пг=5.5 # полуобхвата груди
    Пк=2   # прибавка конструктивная
    Пш=1   # полуобхвата шеи

    # Değerler hesaplanıyor

    Ан  = Ди
    АТ  = Дст
    АГ  = Дст / 4 + Сг / 4 + Пг /4
    ТБ  = Дст / 2 - 2
    ГГ1 = Сг + Пг + Пк
    ГП = Шс + Пг / 2
    ПП1 = Оп / 3 + Пг / 2 + Пк / 2
    АР = Сш / 3 + Пш
    РР1 = АР / 3
    ТП2 = Впс + 2
    Р1П3 = Шп + 0.5
    ПП4 = ПП1 / 2
    ПП5 = ПП1 / 3
    П1П6 = ПП1 / 3 - 1
    П1Г1 = Шг + Пк / 2
    Г1В = Вг
    Т1В = Дпт
    В2П7 = Шп
    ОН = Др - 6.5
    ОВ = ПП1 - 2
    ВВ1 = ПП1 * 3 / 2
    НН1 = ПП1
    ОВ = ПП1
    ВВ1 = ( Оп + 10 ) / 2

    print("\nKalıp ile ilgili")
    print("~~~~~~~~~~~~~")
    print("Ан   : ", round(Ан, 2))
    print("АТ   : ", round(АТ, 2))
    print("АГ   : ", round(АГ, 2))
    print("ТБ   : ", round(ТБ, 2))
    print("ГГ1  : ", round(ГГ1, 2))

    print("\nСпинка")
    print("~~~~~~~~~~~~~")
    print("ГП   : ", round(ГП, 2))
    print("ПП1  : ", round(ПП1, 2))
    print("ПП1  : ", round(ПП1, 2))
    print("АР   : ", round(АР, 2))
    print("РР1  : ", round(РР1, 2))
    print("ТП2  : ", round(ТП2, 2))
    print("Р1П3 : ", round(Р1П3, 2))
    print("ПП4  : ", round(ПП4, 2))
    print("ПП5  : ", round(ПП5, 2))
    print("П1П6 : ", round(П1П6, 2))

    print("\nПолочка")
    print("~~~~~~~~~~~~~")
    print("П1Г1 : ", round(П1Г1, 2))
    print("Г1В  : ", round(Г1В, 2))
    print("Т1В  : ", round(Т1В, 2))
    print("В2П7 : ", round(В2П7, 2))

    print("\nДлинный рукав")
    print("~~~~~~~~~~~~~")
    print("ОН   : ", round(ОН, 2))
    print("ОВ   : ", round(ОВ, 2))
    print("ВВ1  : ", round(ВВ1, 2))
    print("НН1  : ", round(НН1, 2))

    print("\nКороткий рукав")
    print("~~~~~~~~~~~~~")
    print("ОВ   : ", round(ОВ, 2))
    print("ВВ1  : ", round(ВВ1, 2))

start()
