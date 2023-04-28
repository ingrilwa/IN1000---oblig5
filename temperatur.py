""" Oppgave 4, oblig 5 """
""" Funksjon som tar inn en fil og retunerer en ordbok. Oppretter en tom ordbok. Kjører en for-løkke som
iterer gjennom fila. Deler opp linjene med split, og legger verdiene inn i ordbok som nøkler og verdier.
Ordboka returneres."""
def filTilOrdbok(fil):
    ordbok = {}
    for linje in open(fil):
        kolonne = linje.split(",")
        ordbok[kolonne[0]] = float(kolonne[1])
    return ordbok

""" Kaller filTilOrdbok og printer ut ordboka """
varmeste = filTilOrdbok("max_temperatures_per_month.csv")
print(varmeste)

""" Funksjon som tar i mot en ordbok med de høyeste temperaturene og en fil med daglige temperaturer.
I for-løkka iterer vi gjennom og linjene blir igjen splitta og lagt til med tilhørende navn i en ordbok,
måned, dag og temperatur. Så kjører vi en if test som sjekker om temperaturen i den nye filen er høyere enn i den allerede eksisterende orboka. Hvis temperaturen er høyere skriver det ut en setning som forklarer dette,
og temperaturen i ordboka oppdateres til den nå høyeste temperaturen. Så returneres ordboka"""
def varmerekord(ordbok,fil):
    for linje in open(fil):
        kolonne = linje.split(",")
        måned = kolonne[0]
        dag = int(kolonne[1])
        temperatur = float(kolonne[2])
        if temperatur > ordbok[måned]:
            print("Ny varmerekord!", dag, måned, "på", temperatur, "grader celcuis. Forrige rekord var på", ordbok[måned], "grader")
            ordbok[måned] = temperatur
    return ordbok

""" Definerer ny variabel rekord som skriver ut den nye ordboka med de oppdaterte verdiene """
nyOrdbok = varmerekord(varmeste,"max_daily_temperature_2018.csv")
print(nyOrdbok)

""" Funksjon som tar imot en ordbok og et filnavn. Den nye ordboken med de oppdaterte verdiene skrives inn i en ny fil vi kaller "test.txt". Den legger seg i samme mappe vi er i, og jeg går inn og sjekker at den ser ut som den skal. """
def eksporterOrdbok(ordbok,filnavn):
    fil = open(filnavn, "w")
    for måned in ordbok:
        fil.write(måned + "," + str(ordbok[måned]) + "\n")
eksporterOrdbok(varmeste, "test.txt")
