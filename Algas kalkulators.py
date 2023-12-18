print("Esiet sveicinats algas kalkulatora!")
while True:
    try:
        pensionars = int(input("Ja east pensionars, ievasdiet 1, ja nee, tad 2 \n"))
        break
    except ValueError:
        print("Jus esat dolbajobs")
while True:
    try:
        apgadajamie = int(input("Vai Jums ir kads apgadajamais (berns zem 18 gadiem vai kads ar invalidati)? \n "
                                "Ja nav, tad ievadiet 0, ja ir, tad ievadiet cik"))
        break
    except ValueError:
        print("Jus esat dolbajobs")
