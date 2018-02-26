import csv
import re

def main():
    prijzen('prijzen.csv', prijs='turing award', nationaliteit='gri', discipline='INformatica')

def prijzen(location, prijs=None, discipline = None, jaar=None, laureaten=None, motivering=None, nationaliteit = None):
    #Met deze open ik het CSV bestand
    with open(location, 'r') as csvfile:

        #De ingevoerde prijs moet één van deze prijzensoorten zijn
        prijzenSoort = ['nobelprijs', 'abelprijs', 'turing award']
        for prijsInLijst in prijzenSoort:
            if prijs != None and prijs == prijsInLijst:
                prijs = prijs.title()
        if (jaar != None):
            jaar = str(jaar)
        if discipline != None:
            discipline = discipline.lower()

        #Zet de waarde van ingevoerde nationaliteit om naar de HoofdLetters
        if(nationaliteit != None):
            nationaliteit = nationaliteit.upper()
        #Een lijst van alle argumenten
        arguments=[prijs, discipline, jaar,laureaten,motivering, nationaliteit]

        #Een lijst van argumenten die een waarde hebben behalve None
        argumentsAfterCheck = []
        for arg in arguments:
            if(arg != None):
                argumentsAfterCheck.append(arg)

        #Een lijst van alle gevonden rijen die voldoen aan de zoektermen
        rijenVoldoenAanZoekTermen = geefGezochteRijen(csvfile, argumentsAfterCheck)

        #Deze forloop print alle gevonden rijen
        for item in rijenVoldoenAanZoekTermen:
            eenRij = item[0] + ' voor de ' + item[1].title() + ' (' + str(item[2]) + '): ' + str(item[3])

            #De spaties vooraan en achteraan van de string worden verwijderd.
            eenRij = eenRij.lstrip()

            print(eenRij.lstrip())

#Deze functie krijg het CSV bestand en de ingevoerde argumenten mee en controlleert
#Welke rijen in het bestand overeenkomen met de zoektermen. Daarna voegt die dat rij toe aan een
#Lijst. Als alle rijen zojn doorgelopen stuurt deze functie dat lijst terug.
def geefGezochteRijen(csvfile, argumentsAfterCheck):
    readCSV = csv.reader(csvfile, delimiter=';')
    rijen = []

    #Deze forloop doorloopt alle rijen in csvfile
    for row in readCSV:
        #Deze splits de winnaars van de prijs. Als er meerder winnars zijn wordt er een
        #Aparte object van gemaakt.
        lijstLaureaten = row[3].split(",")
        lengteLaureaten = len(lijstLaureaten)

        #Deze variabele krijgt alle nationaliteiten die zich in een rij bevinden.
        nationaliteiten = geefNationaliteitenInEenRij(lengteLaureaten, row[3], lijstLaureaten)

        #Deze variable krijgt aantal overeenkomende kolomen.
        aantalOvereenKomendeArgumenten = geefAantalOvereenkomendeKolomen(argumentsAfterCheck, row, lengteLaureaten, nationaliteiten)

        #Als de lengte gelijk is aan de lengte van de gevraagde argumenten
        if (aantalOvereenKomendeArgumenten == len(argumentsAfterCheck)):

            #Deze rij word toegevoegd aan de lijst
            rijen.append(row)
    return rijen

#Deze functie knipt de nationaliteiten in een rij en zet ze in een string.
#Dit doet door de waardes binnen de parentheses te knippen.
#Aan het einde stuurt deze functie de strings met alle nationaliteiten in een rij terug.
def geefNationaliteitenInEenRij(lengteLaureaten, rij, lijstLaureaten):
    nationaliteiten = ''
    nationaliteitTeller = 0
    while nationaliteitTeller < lengteLaureaten:
        if (rij != 'laureaat'):
            nationaliteiten = nationaliteiten + re.search('\(([^)]+)', lijstLaureaten[nationaliteitTeller]).group(
                1) + ' '
            nationaliteiten = nationaliteiten.upper()
        nationaliteitTeller += 1
    return nationaliteiten


#Deze functie controlleert hoeveel kolomen in een rij overeenkomen met de zoektermen.
#Deze wordt bijgehouden door elke keer als er iets overeenkomt de variabele
#aantalOvereenKomendeArgumenten met een opgehoogd. Aan het eind stuurt deze functie dat variabele terug.
def geefAantalOvereenkomendeKolomen(argumentsAfterCheck, row, lengteLaureaten, nationaliteiten):
    teller = 0
    aantalOvereenKomendeArgumenten = 0
    while (teller < len(argumentsAfterCheck)):
        for kolom in row:
            if row.index(kolom) == 3:
                if argumentsAfterCheck[teller] == lengteLaureaten:
                    aantalOvereenKomendeArgumenten += 1
                elif type(argumentsAfterCheck[teller]) != int \
                        and argumentsAfterCheck[teller] in nationaliteiten:
                    aantalOvereenKomendeArgumenten += 1
            elif row.index(kolom) == 4 and type(argumentsAfterCheck[teller]) != int and \
                            argumentsAfterCheck[teller] in kolom:
                aantalOvereenKomendeArgumenten += 1
            elif type(argumentsAfterCheck[teller]) != int and \
                            argumentsAfterCheck[teller] == kolom:
                aantalOvereenKomendeArgumenten += 1
        teller += 1
    return aantalOvereenKomendeArgumenten

if __name__ == '__main__':
    main()
