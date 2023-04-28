""" Egen oppgave:
Oppgavetekst: Skriv et beregningsprogram for skreddere med en
funksjon som leser inn en fil (som du lager selv og leverer sammen med de andre
filene) der hver linje beskriver et navn på et mål og selve målet i tommer. La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboke'n. Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene i centimeter """

""" Definerer en tom liste mål """
""" Bruker funksjon filTilOrdbok som brukt tidligere i temperatur.py for å legge inn informasjon fra en tekstfil inn i en ordbok i denne filen. Lager på forhånd en tekstfil, skredder.txt som består av mål. Legger ved denne fila. Bruker split() og lagrer navn på målet som nøkkelverdi og målet som innholdsverdi i ordboka. Legger til alle innholdsverdiene fra ordboken i lista kalt mål. Returnerer ordboken."""
mål = []
def filTilOrdbok(fil):
    ordbok = {}
    for linje in open(fil):
        kolonne = linje.split()
        ordbok[kolonne[0]] = float(kolonne[1])
        mål.append(float(kolonne[1]))
    return ordbok

""" Kaller filTilOrdbok og printer ut ordboka """
skreddermål = filTilOrdbok("skredder.txt")
print(skreddermål)

""" Iterer gjennom ordboka med en for-løkke som kjører funksjonen tommerTilCm gjennom hvert element i lista. Bruker samme funksjon tommerTilCm som i regnefunksjoner.py. Printer til slutt ut en setning som forklarer hvor mange centimeter målene i tommer tilsvarer. """
for element in mål:
    def tommerTilCm(element):
        assert element > 0
        return element * 2.54
    print(element, "cm tilsvarer", tommerTilCm(element),"centimeter" )
