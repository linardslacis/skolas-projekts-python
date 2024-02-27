import sys
import matplotlib.pyplot as plt
import numpy as np
import math


# paligfunkcijas
def ievades_validacija(pazinojums, nosacijums, kludas_pazinojums):
    while True:
        try:
            vertiba = float(input(pazinojums))
            if nosacijums(vertiba):
                return vertiba
            else:
                print(kludas_pazinojums)
        except ValueError:
            print("Nederiga ievade. Ludzu, ievadiet derigu skaitlisko vertibu.")


def menu_ievads():
    print("Menu:\n"
          "1. - Netto algas aprēķināšana \n"
          "2. - Hipotekārā kredīta kalkulātors \n"
          "3. - Elastības dažādām funckijām \n"
          "4. - Lidzsvars divam lianeāraām funckijām")
    return ievades_validacija("Jūsu izvēle:",
                              lambda x: x in [1, 2],
                              "Ievadiet derīgu opciju (1 vai 2)")


def turpinat():
    if not ievades_validacija("Vai vēlaties turpināt? \n"
                              "Ja jā, ievadiet 1, ja nē, ievadiet 0!",
                              lambda x: x in [0, 1],
                              "Ievadiet derīgu opciju (1 vai 2)"):
        sys.exit("Paldies, ka izmantojāt mūsu ekonomikas rīku!")


def apgadajamo_parbaude(ap):
    if ap is None:
        ap = ievades_validacija("Ja Jums ir apgadajams personas, ievadiet skaitlu, "
                                "ja nav, ievadiet 0 \n",
                                lambda x: x >= 0,
                                "Ievadiet derīgu naturalo skaitli!")
    else:
        if ievades_validacija("Vai vēlaties mainīt apgadajamo skaitu?"
                              "Ja nē, ievadiet 0, ja jā, ievadiet 1.",
                              lambda x: x in [0, 1],
                              "Lūdzu ievadiet derīgu opciju (0 vai 1)!"):
            ap = ievades_validacija("Ja Jums ir apgadajams personas, ievadiet skaitlu, ja nav, "
                                    "ievadiet 0",
                                    lambda x: x >= 0,
                                    "Ievadiet derīgu naturalo skaitli!")
    return ap


def mnetto_parbaude(mn, ap):
    if mn is None:
        mn = ievades_validacija("Ievadiet savu netto ienākumu summu! Ja zināt tikai brutto ievadiet 0!",
                                lambda x: x >= 0,
                                "Ievadiet derīgu naturalo skaitli!")
        if mn == 0:
            mn = ienakumu_aprekins(ap)
    else:
        if ievades_validacija("Vai vēlaties mainīt ienākumu?"
                              "Ja nē, ievadiet 0, ja jā, ievadiet 1.",
                              lambda x: x in [0, 1],
                              "Lūdzu ievadiet derīgu opciju (0 vai 1)!"):
            mn = ievades_validacija("Ievadiet savu netto ienākumu summu! Ja zināt tikai brutto ievadiet 0!",
                                    lambda x: x >= 0,
                                    "Ievadiet derīgu naturalo skaitli!")
            if mn == 0:
                mn = ienakumu_aprekins(ap)
    return mn


# alga un kredits
def hipotekara_maksajuma_aprekins(kopienak, dsti, summa, termins, iemaksa, prlikme):
    likme = 1 + prlikme + 0.038
    ikmenesa_maksajums = ((summa * likme) - iemaksa) / (12 * termins)

    if ikmenesa_maksajums <= kopienak * dsti:
        print("Jusu ikmenesa maksajums bus:", round(ikmenesa_maksajums, 2))
        return True
    else:
        print("Ikmenesa maksajums ir parak liels. Ludzu, ievadiet datus atkartoti.")
        return False


def dsti_aprekins(kk, kopienakums, apgadajamie):
    if kk <= 0.7:
        return 0.1
    elif 0.7 < kk <= 1:
        return 0.2
    elif 1 < kk <= 2.5:
        dsti = (kopienakums - (492 + 700 * 0.3 * apgadajamie)) / kopienakums
        if apgadajamie == 0:
            if dsti > 0.4:
                return 0.4
            else:
                return dsti
        elif dsti >= 0.4 and apgadajamie != 0:
            if 1.8 < kk <= 2.5:
                return 0.35
            else:
                return 0.3
        else:
            return dsti
    elif kk >= 2.5:
        return 0.4


def ienakumu_aprekins(apgadajamie):
    neapliekamais = float(0)

    pensionars = ievades_validacija("Ja esat pensionars, ievadiet 1, ja ne, tad 0: ",
                                    lambda x: x in [0, 1],
                                    "Ludzu, ievadiet derigu opciju (0 vai 1).")
    invalidate = ievades_validacija("Ja esat invalids, ievadiet grupu(1, 2 vai 3), ja ne, ievadiet 0: ",
                                    lambda x: x in [0, 1, 2, 3],
                                    "Ludzu, ievadiet derigu opciju (0, 1, 2 vai 3).")
    if invalidate == 1 or invalidate == 2:
        atvieglojums = 154
    elif invalidate == 3:
        atvieglojums = 120
    else:
        atvieglojums = 0
    if pensionars != 1:
        atvieglojums = atvieglojums + 250 * apgadajamie

    mbrutto = None
    match ievades_validacija("Ja Jums ir mēnešalga, ievadiet 1, ja stundas likme - 2",
                             lambda x: x in [1, 2],
                             "Ludzu, ievadiet derigu opciju (1 vai 2)."):
        case 1:
            mbrutto = ievades_validacija("Ievadiet savu brutto menesa algu:",
                                         lambda x: x > 0,
                                         "Lūdzu ievadiet derīgu vērtību.")
        case 2:
            stlikme = ievades_validacija("Ievadiet brutto stundas likmi:",
                                         lambda x: x > 0,
                                         "Lūdzu ievadiet derīgu vērtību.")
            stskaits = ievades_validacija("Ievadiet nostradatu stundu skaitu:",
                                          lambda x: x > 0,
                                          "Lūdzu ievadiet derīgu vērtību.")
            mbrutto = stskaits * stlikme

    if neapliekamais + atvieglojums >= mbrutto:
        neapliekamais = mbrutto
        atvieglojums = 0
        print("Jūsu nodokļu atvieglojums ir", mbrutto, "€")
    else:
        print("Jūsu nodokļu atvieglojums ir", neapliekamais + atvieglojums, "€")

    vsaoi = 0.105 * (mbrutto - neapliekamais - atvieglojums)
    print("Jusu vsaoi maksajums ir", round(vsaoi), ".")

    if mbrutto < 20004:
        ii_nk = 0.2
    elif 20004 <= mbrutto < 78100:
        ii_nk = 0.23
    else:
        ii_nk = 0.31
    iin = ii_nk * (mbrutto - neapliekamais - atvieglojums)
    print("Jusu IIN maksajums ir", round(iin), ".")

    nodokli = vsaoi + iin
    print("Kopa nodokli ir", round(nodokli), ".")
    mnetto = mbrutto - iin - vsaoi
    print("Jusu neto alga ir", round(mnetto), ".")
    return mnetto


def hipotekarais(apgadajamie, mnetto):

    lidzaizn = ievades_validacija("Vai jums ir lidzaiznemejs? Ja ir, ievadiet 1, ja nav, ievadiet 0.",
                                  lambda x: x in [0, 1],
                                  "Ludzu, ievadiet derigu opciju (0 vai 1).")
    if lidzaizn == 1:
        print("Ievadiet lidzaiznemeja neto algu:")
        lidzaizn_alga = ievades_validacija("Ievadiet neto algu: ",
                                           lambda x: x > 0,
                                           "Ludzu, ievadiet derigu algu.")
    else:
        lidzaizn_alga = 0

    kopienakums = mnetto + lidzaizn_alga
    kk = kopienakums / 700

    match lidzaizn:
        case 0:
            if mnetto < 850:
                print("Jūsu ienakumi ir parak mazi, lai Jūs varētu atļauties ņemt kredītu!")
                return
        case 1:
            if kopienakums < 1200:
                print("Jūsu ienakumi ir parak mazi, lai Jūs varētu atļauties ņemt kredītu!")
                return

    dsti = dsti_aprekins(kk, kopienakums, apgadajamie)

    # Hipotekaras aizdevuma detaļu ievade un aprekins
    while True:
        summa = ievades_validacija("Ievadiet kredita summu: ",
                                   lambda x: x > 0,
                                   "Ludzu, ievadiet derigu kredita summu.")
        termins = ievades_validacija("Ievadiet kredita terminu gados: ",
                                     lambda x: x > 0,
                                     "Ludzu, ievadiet derigu kredita terminu gados.")
        iemaksa = ievades_validacija("Ievadiet pirmo iemaksu (min 10% no kredita summas): ",
                                     lambda x: 0.1 * summa < x < 0.5 * summa,
                                     "Ludzu, ievadiet derigu pirmo iemaksu.")

        prlikme = ievades_validacija("Ievadiet % likmi ka decimālu: ",
                                     lambda x: -0.1 < x < 1,
                                     "Ludzu, ievadiet derigu procentu likmi.")

        if hipotekara_maksajuma_aprekins(kopienakums, dsti, summa, termins, iemaksa, prlikme):
            break


# elastiba dazadam funckijam
def augstaka_cena():
    while True:
        try:
            maxx = float(input("Ievadiet funckijas lielako cenu: "))
        except ValueError:
            print("Ievadita nepareiza vertiba")
        else:
            if maxx <= 0:
                print("Augstaka cena nevar but vienada vai mazaka par 0")
                continue
            else:
                return maxx


def salidzinasana(t, v):
    if t < 0 or t > v:
        print("Ievadita vertiba atrodas arpus grafika robezam")
        return 1
    elif t == 0:
        print("Cena nevar but vienada ar 0")
        return 1
    else:
        return 0


def nules_parbaude(v, t, a, b, c):
    match t:
        case 1:
            if a*v+b == 0:
                print("Ar doto vertibu nav iespejams aprekinat elastibu")
                return 1
            else:
                return 0
        case 2:
            if a * v ** 2 + b * v + c == 0:
                print("Ar doto vertibu nav iespejams aprekinat elastibu")
                return 1
            else:
                return 0
        case 3:
            if a * math.e ** (v * b) + c == 0:
                print("Ar doto vertibu nav iespejams aprekinat elastibu")
                return 1
            else:
                return 0
        case 4:
            if a * pow(v, 0.5) + b == 0:
                print("Ar doto vertibu nav iespejams aprekinat elastibu")
                return 1
            else:
                return 0


def cenas(m2, t, a, b, c):
    while True:
        while True:
            c2 = ievades_validacija("Lai aprekinatu elastibu, ievadiet pirmo cenu: ",
                                    lambda q: q == float,
                                    "Ievadiet derīgu skaitlisko vērtību!")
            if salidzinasana(c2, m2) == 0 and nules_parbaude(c2, t, a, b, c) == 0:
                break
        while True:
            c3 = ievades_validacija("Ievadiet otro cenu: ",
                                    lambda q: q == float,
                                    "Ievadiet derīgu skaitlisko vērtību!")
            if salidzinasana(c3, m2) == 0 and nules_parbaude(c3, t, a, b, c) == 0:
                break

        if c2 > c3:
            c2, c3 = c3, c2
            break
        elif c2 == c3:
            print("Ievaditas vertibas ir vienadas")
        else:
            break
    return c2, c3


def elastiba(v0, v1, q0, q1):
    el = ((q1 - q0) / q0) / ((v1 - v0) / v0)
    if abs(el) == 1:
        print("Elastiba = |1|, pieprasijums ir vienadots")
    elif abs(el) < 1:
        print("Elastiba =", round(abs(el)), ", pieprasijums ir neelastigs")
    else:
        print("Elastiba =", round(abs(el)), ", pieprasijums ir elastigs")
    return None


def elastibas_aprekins():
    a, b, c = 0, 0, 0
    x = np.linspace(0, augstaka_cena(), 100)
    match ievades_validacija("Izveleties velamo funkciju: \n 1. lineara \n "
                             "2. kvadratiska \n 3. eksponente \n 4. kvadratsakne(radikals)",
                             lambda q: q in [1, 2, 3, 4],
                             "Ievadiet derīgu opciju(1, 2, 3 vai 4"):
        case 1:
            print("Jusu izveleta funkcija: ax + b")
            a = ievades_validacija("Ievadiet a: ",
                                   lambda q: q == float,
                                   "")
            b = ievades_validacija("Ievadiet b: ",
                                   lambda q: q == float,
                                   "")
            y = a * x + b
            c0, c1 = cenas(x[99], 1, a, b, c)
            y0 = a * c0 + b
            y1 = a * c1 + b
            elastiba(c0, c1, y0, y1)

        case 2:
            print("Jusu izveleta funkcija: ax^2 * bx + c")
            a = ievades_validacija("Ievadiet a: ",
                                   lambda q: q == float,
                                   "")
            b = ievades_validacija("Ievadiet b: ",
                                   lambda q: q == float,
                                   "")
            c = ievades_validacija("Ievadiet c: ",
                                   lambda q: q == float,
                                   "")
            y = a * x ** 2 + b * x + c
            c0, c1 = cenas(x[99], 2, a, b, c)
            y0 = a * c0 ** 2 + b * x + c
            y1 = a * c1 ** 2 + b * x + c
            elastiba(c0, c1, y0, y1)

        case 3:
            print("Jusu izveleta funkcija: ae^(bx) + c")
            a = ievades_validacija("Ievadiet a: ",
                                   lambda q: q == float,
                                   "")
            b = ievades_validacija("Ievadiet b: ",
                                   lambda q: q == float,
                                   "")
            c = ievades_validacija("Ievadiet c: ",
                                   lambda q: q == float,
                                   "")
            y = a * math.e ** (x * b) + c
            plt.ylim(0, 100)
            c0, c1 = cenas(x[99], 3, a, b, c)
            y0 = a * math.e ** (c0 * b) + c
            y1 = a * math.e ** (c1 * b) + c
            elastiba(c0, c1, y0, y1)

        case 4:
            print("Jusu izveleta fukcija ir: a√x + b")
            a = ievades_validacija("Ievadiet a: ",
                                   lambda q: q == float,
                                   "")
            b = ievades_validacija("Ievadiet b: ",
                                   lambda q: q == float,
                                   "")
            y = a * pow(x, 0.5) + b
            c0, c1 = cenas(x[99], 4, a, b, c)
            y0 = a * pow(c0, 0.5) + b
            y1 = a * pow(c1, 0.5) + b
            elastiba(c0, c1, y0, y1)

    # noinspection PyUnboundLocalVariable
    plt.plot(x, y)
    plt.xlabel('x, Cena')
    plt.ylabel('y, Daudzums')
    plt.grid(True)
    plt.show()


# lidzsvars
def koeficientm(a11, a12, c11, c12):
    m3 = (c12-c11)/(a12-a11)
    b3 = c11-(a11*m3)
    return m3, b3


def krustpunkts(a4, b4, a8, b8):
    if a4 == a8:
        print("Liknes ir paralelas")
        return None
    x5 = (b8 - b4) / (a4 - a8)
    y5 = a4 * x5 + b4
    return x5, y5


def pagarinajums_pa_kreisi(k, l1, h):
    if l1 == 0:
        return h
    else:
        return h - l1 * k


def pagarinajums_pa_labi(k, l1, h, xlim):
    if l1 == 2 * xlim:
        return h
    else:
        return h + (2 * xlim-l1) * k


def lidzsvars_aprekins():
    x11 = ievades_validacija("Ievadiet daudzumu pirmajam pieprasījuma punktam: ",
                             lambda q: q == float,
                             "")
    y11 = ievades_validacija("Ievadiet atbilstošo cenu: ",
                             lambda q: q == float,
                             "")
    x12 = ievades_validacija("Ievadiet daudzumu otrajam pieprasījuma punktam: ",
                             lambda q: q == float,
                             "")
    y12 = ievades_validacija("Ievadiet atbilstošo cenu: ",
                             lambda q: q == float,
                             "")

    x21 = ievades_validacija("Ievadiet daudzumu pirmajam piedavājuma punktam: ",
                             lambda q: q == float,
                             "")
    y21 = ievades_validacija("Ievadiet atbilstošo cenu: ",
                             lambda q: q == float,
                             "")
    x22 = ievades_validacija("Ievadiet daudzumu otrajam piedavājuma punktam: ",
                             lambda q: q == float,
                             "")
    y22 = ievades_validacija("Ievadiet atbilstošo cenu: ",
                             lambda q: q == float,
                             "")

    # koeficientu un krustpunktu aprekini
    k_pieprasijums, b_pieprasijums = koeficientm(x11, x12, y11, y12)

    k_piedavajums, b_piedavajums = koeficientm(x21, x22, y21, y22)

    x, y = krustpunkts(k_pieprasijums, b_pieprasijums, k_piedavajums, b_piedavajums)

    print("Lidzsvara daudzums ir ", x, " vienibas, un atbilstosa cena ir ", y)

    # elastiba
    pc0, d = (int(input("Lai aprekinatu elastibu ievadiet cenu: ")), int(input("Ievadiet cenas izmainu procentos: ")))
    pc1 = pc0 * (1 + (d / 100))
    pq0 = (pc0 - b_pieprasijums) / k_pieprasijums
    pq1 = (pc1 - b_pieprasijums) / k_pieprasijums

    e = ((pq1 - pq0) / pq0) / ((pc1 - pc0) / pc0)
    if abs(e) == 1:
        print("Elastiba = |1|, tatad pieprasijums ir vienadots")
    elif abs(e) < 1:
        print("Elastiba =", abs(e), ", pieprasijums ir neelastigs")
    else:
        print("Elastiba =", abs(e), ", pieprasijums ir elastigs")

    # funkciju punkti
    x_pieprasijums = np.array([0, x * 2])
    y_pieprasijums = np.array([pagarinajums_pa_kreisi(k_pieprasijums, x11, y11),
                               pagarinajums_pa_labi(k_pieprasijums, x12, y12, x)])

    x_piedavajums = np.array([0, x * 2])
    y_piedavajums = np.array([pagarinajums_pa_kreisi(k_piedavajums, x21, y21),
                              pagarinajums_pa_labi(k_piedavajums, x22, y22, x)])

    x_krustpunkts = np.array([x, x, x])
    y_krustpunkts = np.array([y * 2, y, 0])

    # funkciju attelosana
    plt.plot(x_pieprasijums, y_pieprasijums, label="Pieprasijums")
    plt.plot(x_piedavajums, y_piedavajums, label="Piedavajums")
    plt.plot(x_krustpunkts, y_krustpunkts, marker='o', label="Lidzsvars")
    plt.legend(loc='upper center')

    # grafika ipasibas
    plt.xlim(0, x * 2)
    plt.ylim(0, y * 2)
    plt.title("Pieprasījuma, piedāvājuma likne")
    plt.xlabel("Daudzums")
    plt.ylabel("Cena")
    plt.grid()
    plt.show()
