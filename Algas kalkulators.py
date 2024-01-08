print("Esiet sveicinats algas kalkulatora!") # jaizveido saraksts ar neapliekamajiem ienakumiem
while True:
    try:
        pensionars = int(input("Ja east pensionars, ievasdiet 1, ja nee, tad 2 \n")) #pensionareim neatliekamais minimums ir 500 eur
        break
    except ValueError:
        print("Jus kaut ko esat ievadijis nepareizi!")
while True:
    try:
        apgadajamie = int(input("Vai Jums ir kads apgadajamais (berns zem 18 gadiem vai kads ar invalidati)? \n "
                                "Ja nav, tad ievadiet 0, ja ir, tad ievadiet cik"))  # max apgadajamo skaits vienai personai nav noradits, pensionari parasti nevar sanemt 250 apgadajama ativieglojumu
        break
    except ValueError:
        print("Jus kaut ko esat ievadijis nepareizi!")
#pec algas kalkulatora uztaisit hipotekaro kreditu kalkulatoru no dotas informacijas, kur parada izdevigako kreditu kuru var nemt ar savu algu un 2 cilveku algam
#hipotekaro kreditu kalkulatora ieklaut procentu likmes un izdevigaku kreditu veidus ja nem no citam pilsetam piemeram kuldigas seb bankas
#personas ar I vai II grupas invaliditati vai politiski represetie 154 eur nodoklu atvieglojums, III grupas 120 eur
#max neapliekamais minimums ir ienakumiem lidz 500 eur un NM ( neapliekamais minimums )vairs nav pie 1800 f-ja y= -0,385x +692,308 ( strada tikai robezas no 500 lidz 1800eur, ja zem 500 tad viss neapliekams)
#Uztaisit sarakstu ar neapliekamajiem ienakumiem un pec tam taisit kreditu pamacibu
#Progresīvais iedzīvotāju ienākuma nodoklis: ienākumam līdz 20 004, eiro – 20 %, ienākumam no 20 004 eiro līdz 78 100 eiro – 23 %; ienākuma daļai, kas pārsniedz 78 100 eiro – 31 %.
#10,50 % darba ņēmējs maksa socialo nodokli (parasti) jeb  VSAOI