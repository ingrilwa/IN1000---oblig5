""" Oppgave 2, oblig 5 """

""" Funksjon som returnerer brukernavn av et fullt navn """
def lagBrukernavn(fulltNavn):
    navn = fulltNavn.split(" ")
    fornavn = navn[0]
    etternavn = navn[1]
    brukernavn = str.lower(fornavn) + str.lower(etternavn[0])
    return brukernavn

""" Funksjon som returnerer epost av prefix og suffix """
def lagEpost(prefix,suffix):
    epost = prefix + "@" + suffix
    return epost

""" Funksjon som skriver ut eposter med verdier fra en ordbok. Prefix er nøkkelverdi og suffix er innholdsverdi
Verdiene og funksjonen kjører gjennom funksjonen lagEpost og printer resultatet."""
def skrivUtEposter(ordbok):
    for prefix in ordbok:
        print(lagEpost(prefix,ordbok[prefix]))

""" Tester ut funksjonen lagBrukernavn med mitt eget navn """
print(lagBrukernavn("Ingrid Ljosland"))

""" Tester ut funksjonen skrivUtEposter med en testordbok fra oppgaveteksten """
testordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}
skrivUtEposter(testordbok)

""" Lager først en tom ordbok. Lager while-løkke som kjører så lenge variabelen kommando ikke er s.
I while-løkka er det en if-test som sjekker hva brukeren skriver inn. Så lenge brukeren skriver "i" skal
programmet kjøre og spørre om fullt navn og suffix og lage et brukernavn gjennom funksjonen lagBrukernavn.
Dette legges til i den tomme ordboken. Hvis bruker skriver "p",skal ordboken printes med alle epostene.
Når bruker skriver "s" stopper while-løkka."""
ordbok = {}
kommando = ""
while kommando != "s":
    kommando = input("Kommando: ")
    if kommando == "i":
        print("Legg til en bruker")
        fulltNavn = input("Fullt navn: ")
        suffix = input("Suffix: ")
        brukernavn = lagBrukernavn(fulltNavn)
        ordbok[brukernavn] = suffix
    elif kommando == "p":
        skrivUtEposter(ordbok)
