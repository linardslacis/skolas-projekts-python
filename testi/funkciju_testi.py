while True:
    while True:
        try:
            print("Izveleties velamo funkciju: \n 1. lineara \n 2. kvadratiska \n 3. eksponente \n 4. kvadratsakne("
                  "radikals)")
            izvele = int(input())
            break
        except ValueError:
            print("Ievadita nepareiza vertiba")
    if 1 <= izvele <= 4:
        break
    else:
        print("Ievadita nepareiza vertiba")
print("Viss")
