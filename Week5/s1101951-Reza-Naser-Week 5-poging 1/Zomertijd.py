import sys
import calendar
import datetime
from datetime import date, timedelta, datetime

def main():
    klok('27/10/2007')

#Deze functie krijgt het jaartal als verplichte parameter mee.
#Daarna berekent die de laatste zondag van het jaar en maand.
#De maand waar de wintertijd beeindigt is altijd maand 3.
#Daarom is krijgt de variabele maand de waarde 3.
#De functie maakt een date object en stuurt deze dan terug.
def zomertijd(jaartal):
    maand = 3
    jaar = controlleerJaar(jaartal)
    laatsteZondagInMaart = max(week[-1] for week in calendar.monthcalendar(jaar, maand))
    zondagDatum = date(jaar,maand, laatsteZondagInMaart)
    return zondagDatum

#Deze functie krijgt het jaartal als verplichte parameter mee.
#Daarna berekent die de laatste zondag van het jaar en maand.
#De maand waar de zomertijd beeindigt is altijd maand 10.
#Daarom is krijgt de variabele maand de waarde 10.
#De functie maakt een date object en stuurt deze dan terug.
def winterTijd(jaartal):
    maand = 10
    jaar = controlleerJaar(jaartal)
    laatsteZondagInOktober = max(week[-1] for week in calendar.monthcalendar(jaar, maand))
    zondagDatum = date(jaar,maand, laatsteZondagInOktober)
    return zondagDatum


#Deze functie converteert eerst de ingevoerde datum in een date object.
#Daarna vraagt die de zomertijd en de wintertijd terug door gebruik te maken van bovengemaakte functies.
#De functie vergelijkt de date object en bepaalt zo of het om omschakkeling, zomertijd of wintertijd gaat.
def klok(datum):
    datumConverted = datetime.strptime(datum, "%d/%m/%Y")
    datumConverted = datetime.date(datumConverted)
    zomerTijd = zomertijd(datumConverted.year)
    wintertijd = winterTijd(datumConverted.year)
    if datumConverted > zomerTijd and datumConverted < wintertijd:
        print('zomertijd')
    elif datumConverted == zomerTijd:
        print('omschakeling van wintertijd naar zomertijd')
    elif datumConverted == wintertijd:
        print('omschakeling van zomertijd naar wintertijd')
    elif datumConverted > wintertijd or datumConverted < zomerTijd:
        print('wintertijd')


def controlleerJaar(jaartal):
    if jaartal >= 1600 and jaartal <= 2400:
        return jaartal
    else:
        print("Het jaartal is tehoog/telaag")


if __name__ == '__main__':
    main()
