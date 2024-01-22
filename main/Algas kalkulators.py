

def parbaude():
    while True:
        try:
            t = int(input())
            return t
        except ValueError:
            print("Ievadita nepareiza vertiba")

#jaizveido saraksts ar neapliekamajiem ienakumiem
print("Esiet sveicinats algas kalkulatora!")

#pensionareim neatliekamais minimums ir 500 eur
print("Ja esat pensionars, ievasdiet 1, ja nee, tad 2 \n")
while True:
    pensionars = parbaude()
    if 0 < pensionars < 3:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

print("Ja Jums ir invalidāte, ievadiet grupu(1, 2 vai 3), ja nav, ievadiet 4")
while True:
    invalidate = parbaude()
    if 0 < invalidate < 5:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

# max apgadajamo skaits vienai personai nav noradits, pensionari parasti nevar sanemt 250 apgadajama ativieglojumu
print("Vai Jums ir kads apgadajamais (berns zem 18 gadiem vai kads ar invalidati)? \n "
                                "Ja nav, tad ievadiet 0, ja ir, tad ievadiet cik")
while True:
    apgadajamie = parbaude()
    if apgadajamie >= 0:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

print("Ja Jums ir mēnešalga, ievadiet 1, ja stundas likme - 2: ")
while True:
    algastips = parbaude()
    if 0 < algastips < 3:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

match algastips:
    case 1:
        print("Ievadiet savu brutto menesa algu:")
        while True:
            malga = parbaude()
            if malga > 0:
                break
            else:
                print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")
    case 2:
        print("Ievadiet brutto stundas likmi:")
        while True:
            stlikme = parbaude()
            if stlikme > 0:
                break
            else:
                print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")
        print("Ievadiet nostradatu stundu skaitu:")
        while True:
            stskaits = parbaude()
            if stskaits > 0:
                malga = stskaits * stlikme
                break
            else:
                print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

alga = malga * 12






#pec algas kalkulatora uztaisit hipotekaro kreditu kalkulatoru no dotas informacijas, kur parada izdevigako kreditu kuru var nemt ar savu algu un 2 cilveku algam
#hipotekaro kreditu kalkulatora ieklaut procentu likmes un izdevigaku kreditu veidus ja nem no citam pilsetam piemeram kuldigas seb bankas
#personas ar I vai II grupas invaliditati vai politiski represetie 154 eur nodoklu atvieglojums, III grupas 120 eur
#max neapliekamais minimums ir ienakumiem lidz 500 eur un NM ( neapliekamais minimums )vairs nav pie 1800 f-ja y= -0,385x +692,308 ( strada tikai robezas no 500 lidz 1800eur, ja zem 500 tad viss neapliekams)
#Uztaisit sarakstu ar neapliekamajiem ienakumiem un pec tam taisit kreditu pamacibu
#Progresīvais iedzīvotāju ienākuma nodoklis: ienākumam līdz 20 004, eiro – 20 %, ienākumam no 20 004 eiro līdz 78 100 eiro – 23 %; ienākuma daļai, kas pārsniedz 78 100 eiro – 31 %.
#10,50 % darba ņēmējs maksa socialo nodokli (parasti) jeb  VSAOI, mainas atkariba no vecuma un ienakumu daudzuma, veselibas stavokla