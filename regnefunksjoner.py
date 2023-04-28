""" Oppgave 1, oblig 5 """

""" Funksjon som returnerer summen av to tall """
def addisjon(a,b):
    return a + b
    
""" Printer og kaller på funksjonen med to heltall """
print(addisjon(5,7))

""" Funksjon som returnerer differansen av to tall """
def subtraksjon(a,b):
    return a - b

""" Funksjon som returnerer et tall dividert med et annet """
def divisjon(a,b):
    return a / b

""" Tester funksjonen subtraksjon ved hjelp av assert  """
assert subtraksjon(8,3) == 5
assert subtraksjon(-7,3) == -10
assert subtraksjon(-6,-5) == -1

""" Tester funksjonen divisjon ved hjelp av assert  """
assert divisjon(8,2) == 4
assert divisjon (-12,-6) == 2
assert divisjon(-80,2) == -40

""" Funksjon som konverterer fra tommer til centimeter og retunerer dette """
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54
print(tommerTilCm(10))

""" Funksjon som gjør beregninger ved hjelp av de tidligere skrevne funksjonene, addisjon, subtraksjon,
divisjon og tommerTilCm med tall fra brukerinput. """
def skrivBeregninger():
    print("Utregninger:")
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    print("Resultat av summering:", addisjon(tall1,tall2))
    print("Resultat av subtraksjon:", subtraksjon(tall1,tall2))
    print("Resultat av divisjon:", divisjon(tall1,tall2))
    print("Konvertering fra tommer til centimeter:")
    tall3 = float(input("Skriv inn antall tommer"))
    print(tall3, "tommer tilsvarer", tommerTilCm(tall3), "centimeter")

skrivBeregninger()
