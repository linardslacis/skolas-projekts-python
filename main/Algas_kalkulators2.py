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


def hipotekara_maksajuma_aprekins(kopienak, dsti, summa, termins, iemaksa, prlikme):
    likme = 1 + prlikme + 0.038
    ikmenesa_maksajums = ((summa * likme) - iemaksa) / (12 * termins)

    if ikmenesa_maksajums <= kopienak * dsti:
        print("Jusu ikmenesa maksajums bus:", round(ikmenesa_maksajums, 2))
        return True
    else:
        print("Ikmenesa maksajums ir parak liels. Ludzu, ievadiet datus atkartoti.")
        return False


def galvenais():
    neapliekamais = float(0)
    print("Esiet sveicinats algas kalkulatora!")

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
    apgadajamie = ievades_validacija("Ja jums ir kāds apgadajamais, ievadiet to skaitu, ja nav, ievadiet 0: ",
                                     lambda x: x >= 0,
                                     "Ludzu, ievadiet derigu opciju (naturalo skaitli vai 0).")
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

    # Hipotekaras maksajuma sadala
    if ievades_validacija("Vai velaties izmantot hipotekara kredita pakalpojumus? Ievadiet 1, ja jā, ja nē, tad 0.",
                          lambda x: x in [0, 1],
                          "Ievadiet derīgu opciju (0 vai 1") == 0:
        sys.exit("Paldies, ka izvelejaties musu algas kalkulatoru!")

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
    if kk <= 0.7:
        dsti = 0.1
    elif 0.7 < kk <= 1:
        dsti = 0.2
    elif 1 < kk <= 2.5:
        if kopienakums * 0.6 >= 492 + 210 * apgadajamie:
            dsti = 0.4
        else:
            dsti = (kopienakums - (492 + 700 * 0.3 * apgadajamie)) / kopienakums
            if dsti > 0.4:
                dsti = 0.4
    elif kk >= 2.5:
        dsti = 0.4

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

    sys.exit("Paldies, ka izvēlējaties mūsu hipotekāro kredītoru!")


if __name__ == "__main__":
    galvenais()
