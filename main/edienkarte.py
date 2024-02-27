from menu_paligfunkcijas import *


apgadajamie, mnetto = None, None


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

        case 3:
            elastibas_aprekins()

        case 4:
            lidzsvars_aprekins()

    turpinat()
