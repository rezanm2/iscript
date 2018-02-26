from math import *
import math

def berekenPoolCordinaten():
    #Vraagt de x cordinaat. x zet de waarde van input om naar float
    x = float(input("Voer de x coordinaat in: "))

    #Vraagt de y cordinaat. y zet de waarde van input om naar float
    y = float(input("Voer de y coordinaat in: "))

    #Standaard functie van math die de straal berekent
    straal = math.hypot(x, y)
    print ("De straal is: ",straal)
    #Standaard functie van math die de hoek berekent
    hoek = math.atan2(y, x)
    print ("De hoek is: ", hoek)

if __name__ == '__main__':
    berekenPoolCordinaten()