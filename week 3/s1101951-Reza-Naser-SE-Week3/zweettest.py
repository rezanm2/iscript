

def testTaaislijmziekte():
    leeftijdInMaanden = int(input('Geef leeftijd in maanden : '))
    chlorideconcentratie = int(input('Geef chlorideconcentratie in mmol/L : '))

#Volgende if-statement controleert de leetijd in maanden en chlorideconcentratie
    if leeftijdInMaanden <= 6:
        if chlorideconcentratie <= 29:
            diagnose = 'CF is hoogst onwaarschijnlijk'
        elif chlorideconcentratie <= 59:
            diagnose = 'CF is mogelijk'
        else:
            diagnose = 'CF is waarschijnlijk'

    else:
        if chlorideconcentratie <= 39:
            diagnose = 'CF is hoogst onwaarschijnlijk'
        elif chlorideconcentratie <= 59:
            diagnose = 'CF is mogelijk'
        else:
            diagnose = 'CF is waarschijnlijk'

    print(diagnose)

if __name__ == '__main__':
    testTaaislijmziekte()