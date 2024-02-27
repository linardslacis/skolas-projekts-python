import sys


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
          "2. - Hipotekārā kredīta kalkulātors")
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
    if ap < 0:
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
    if mn < 0:
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

    algastips = ievades_validacija("Ja Jums ir mēnešalga, ievadiet 1, ja stundas likme - 2",
                                   lambda x: x in [1, 2],
                                   "Ludzu, ievadiet derigu opciju (1 vai 2).")
    match algastips:
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
