from menu_paligfunkcijas import *


apgadajamie = int(-1)
mnetto = float(-1)


print("Esiet sveicināti multifunkcionalajā ekonomikas rīkā!")
while True:
    t = menu_ievads()
    match t:
        case 1:
            apgadajamie = apgadajamo_parbaude(apgadajamie)
            mnetto = ienakumu_aprekins(apgadajamie)

        case 2:
            apgadajamie, mnetto = apgadajamo_parbaude(apgadajamie), mnetto_parbaude(mnetto, apgadajamie)
            hipotekarais(apgadajamie, mnetto)

    turpinat()
