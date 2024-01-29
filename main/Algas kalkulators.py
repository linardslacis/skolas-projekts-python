
def parbaude():
    while True:
        try:
            t = float(input())
            return t
        except ValueError:
            print("Ievadita nepareiza vertiba")


print("Esiet sveicinats algas kalkulatora!")

neapliekamais = float(0)

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
        if invalidate == 1 or 2:
            atvieglojums = 154
        elif invalidate == 3:
            atvieglojums = 120
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

# max apgadajamo skaits vienai personai nav noradits, pensionari parasti nevar sanemt 250 apgadajama ativieglojumu
print("Vai Jums ir kads apgadajamais (berns zem 18 gadiem vai kads ar invalidati)? \n "
      "Ja nav, tad ievadiet 0, ja ir, ievadiet 1")
while True:
    apgadajamie = parbaude()
    if 0 <= apgadajamie < 2:
        if pensionars == 2:
            atvieglojums += 250
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
            mbrutto = parbaude()
            if mbrutto > 0:
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
                mbrutto = stskaits * stlikme
                break
            else:
                print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

if mbrutto < 700:
    neapliekamais = mbrutto
elif mbrutto > 1800:
    neapliekamais = 0
else:
    neapliekamais = 692.308 - 0.385 * mbrutto
print("Jusu neapliekamais minimums ir", round(neapliekamais),".")

VSAOI = 0.105 * (mbrutto - neapliekamais - atvieglojums)
print("Jusu VSAOI maksajums ir", round(VSAOI),".")

if mbrutto < 20004:
    IINk = 0.2
elif 20004 <= mbrutto < 78100:
    IINk = 0.23
else:
    IINk = 0.31
IIN = IINk * (mbrutto - neapliekamais - atvieglojums)
print("Jusu IIN maksajums ir", round(IIN),".")

nodokli = VSAOI + IIN
print("Kopa nodokli ir", round(nodokli),".")
mnetto = mbrutto - IIN - VSAOI
print("Jusu neto alga ir", round(mnetto),".")