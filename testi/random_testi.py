while True:
    mnetto = int(input("netto alga:"))
    if mnetto == 0:
        break
    apgadajamie = int(input("apgadajamie:"))

    if mnetto * 0.6 >= 492 + 210 * apgadajamie:
        dsti = 0.4
    else:
        dsti = (mnetto - (492 + 700 * 0.3 * apgadajamie)) / mnetto

    print("DSTI:", round(dsti * 100), "%")
