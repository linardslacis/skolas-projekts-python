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

def galvenais(apgadajamie, mnetto):
    if not bool(apgadajamie):
        apgadajamie = ievades_validacija("Ievadiet apgadajamu skaitu vai 0, ja tādu nav.",
                                         lambda x: x >= 0,
                                         "Ievadiet derīgu naturālo skaitli!")
    if not bool(mnetto):
        mnetto = ievades_validacija("Ievadiet savus ienākumus: ",
                                    lambda x: x > 0,
                                    "Ievadiet derīgu pozitīvu skaitli!")

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

    if apgadajamie == -1:
        apgadajamie = ievades_validacija("Ievadiet apgadajamo skaitu, ja tādu nav, ievadiet 0.",
                                         lambda x: x >= 0,
                                         "Ievadiet terīgu naturalu skaitli")

    kopienakums = mnetto + lidzaizn_alga
    kk = kopienakums / 700

    match lidzaizn:
        case 0:
            if mnetto < 850:
                sys.exit("Jūsu ienakumi ir parak mazi, lai Jūs varētu atļauties ņemt kredītu!")
        case 1:
            if kopienakums < 1200:
                sys.exit("Jūsu ienakumi ir parak mazi, lai Jūs varētu atļauties ņemt kredītu!")

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

    sys.exit("Paldies, ka izvēlējaties mūsu hipotekāro kredītoru!")

