
def parbaude():
    while True:
        try:
            t = float(input())
            return t
        except ValueError:
            print("Ievadita nepareiza vertiba")


print("Esiet sveicinats algas kalkulatora!")

neapliekamais = float(0)

print("Ja esat pensionars, ievasdiet 1, ja nee, tad 0")
while True:
    pensionars = parbaude()
    if 0 <= pensionars <= 1:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

print("Ja Jums ir invalidāte, ievadiet grupu(1, 2 vai 3), ja nav, ievadiet 0")
while True:
    invalidate = parbaude()
    if 0 <= invalidate < 4:
        if invalidate == 1 or invalidate == 2:
            atvieglojums = 154
        elif invalidate == 3:
            atvieglojums = 120
        else:
            atvieglojums = 0

        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

# max apgadajamo skaits vienai personai nav noradits, pensionari parasti nevar sanemt 250 apgadajama ativieglojumu
print("Vai Jums ir kads apgadajamais (berns zem 18 gadiem vai kads ar invalidati)? \n "
      "Ja nav, tad ievadiet 0, ja ir, ievadiet skaitu")
while True:
    apgadajamie = parbaude()
    if apgadajamie >= 0:
        if pensionars == 1:
            break
        else:
            atvieglojums = atvieglojums + 250 * apgadajamie
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

if mbrutto < 500:
    neapliekamais = mbrutto
elif mbrutto > 1800:
    neapliekamais = 0
else:
    neapliekamais = 692.308 - 0.385 * mbrutto
print("Jusu neapliekamais minimums ir", round(neapliekamais), ".")
print("Jūsu nodokļu atvieglojums ir", round(atvieglojums), ".")

if neapliekamais + atvieglojums >= mbrutto:
    neapliekamais = mbrutto
    atvieglojums = 0

VSAOI = 0.105 * (mbrutto - neapliekamais - atvieglojums)
print("Jusu VSAOI maksajums ir", round(VSAOI), ".")

if mbrutto < 20004:
    IINk = 0.2
elif 20004 <= mbrutto < 78100:
    IINk = 0.23
else:
    IINk = 0.31
IIN = IINk * (mbrutto - neapliekamais - atvieglojums)
print("Jusu IIN maksajums ir", round(IIN), ".")

nodokli = VSAOI + IIN
print("Kopa nodokli ir", round(nodokli), ".")
mnetto = mbrutto - IIN - VSAOI
print("Jusu neto alga ir", round(mnetto), ".")

#hipotekarais
print("Vai velaties izmantot hipotekāra kreditora pakalpojumus?")
print("Vai jums ir lidzaiznemejs? Ja ir, ievadiet 1, ja nav, ievadiet 0")
while True:
    lidzn = parbaude()
    if lidzn == 0 or lidzn == 1:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

print("Ievadiet lidzaiznemeja netto algu:")
while True:
    lidznalga = parbaude()
    if lidznalga > 0:
        break
    else:
        print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

kopienak = mnetto + lidznalga
kk = kopienak / 700
if kk <= 0.7:
    dsti = 0.1
elif 0.7 < kk <= 1:
    dsti = 0.2
elif 1 < kk <= 2.5:
    if kopienak * 0.6 >= 492 + 210 * apgadajamie:
        dsti = 0.4
    else:
        dsti = (kopienak - (492 + 700 * 0.3 * apgadajamie)) / kopienak
        if dsti > 0.4:
            dsti = 0.4
elif kk >= 2.5:
    dsti = 0.4
while True:
    print("Ievadiet kredita summu: ")
    while True:
        summa = parbaude()
        if summa > 0:
            break
        else:
            print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

    print("Ievadiet kredita terminu gados: ")
    while True:
        termins = parbaude()
        if termins > 0:
            break
        else:
            print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")

    print("Ievadiet pirmo iemaksu (min 10% no kredita summas): ")
    while True:
        iemaksa = parbaude()
        if summa * 0.1 < iemaksa < 0.5 * summa:
            break
        else:
            print("Meginiet ievadit atkartoti, iemaksa bija par mazu vai par lielu:)")

    print("Ievadiet % likmi kā dalskaitli: ")
    while True:
        prlikme = parbaude()
        if -0.1 < prlikme < 1:
            break
        else:
            print("Meginiet ievadit atkartoti, kaut kas nebija kartiba :)")
    likme = 1 + prlikme + 0.038

    if summa * likme / (12 * termins) <= kopienak * dsti:
        print("Jusu ikmenesa maksujums bus:", summa * likme / (12 * termins))
        break
    else:
        print("Ikmenesa meksajums ir parak liels, meginiet ievadit datus atkartoti")


#Lai noteiktu hip. kredīta summu ir nepieciešams ievadei neto alga, no tās aprēķina koeficientu jeb neto alga/ min bruto algas kas ir 700 sogad
# vēl nepieciesams zinat apgadajamo skaits un kredita ilgums gados (par katru apgadajamo bernu jaatstaj 30% no bruto algas jeb max 60%)
#kredītņēmējam nevar palikt mazāk par 80% no valsts minimālās algas jeb 700*0,8 = 560 eur uz rokas
# kreditu var nemt kopa ar laulato
#https://stat.gov.lv/lv/statistikas-temas/iedzivotaji/majsaimniecibu-izdevumi un Pārliecināties par patērētāja maksātspēju ārpus Vadlīniju DSTI tabulā noteiktajiem
#limitiem (t.sk. izmantojot citu vērtēšanas metodoloģiju) var, izvērtējot patērētāja
# regulāro izdevumu paradumus un apmērus (piemēram, vērtējot
#bankas konta izdruku), tai skaitā, noskaidrojot apgādājamo skaitu, iespējamos īres
#maksājumus, kā arī izmantojot Centrālās statistikas pārvaldes publicētos datus par
#vidējiem patēriņa izdevumu apmēriem attiecīgajā izmaksu kategorijā
