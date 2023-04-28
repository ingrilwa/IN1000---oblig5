""" Oppgave 3, oblig 5 """
""" Først definereres funksjonen minFunksjon(). Så defineres funksjonen hovedprogram(). Så kalles funksjonen
hovedprogram på. Inne i funksjonen hovedprogram defineres først en variabel a til å være 42. Så defineres b
til 0. Deretter printer b ut, og det vil altså printes 0. Så settes b lik a, og b endrer sin verdi fra 0 til 42.
Så settes a lik en fuksjon minFunksjon, og denne funksjonen kalles på. I minFunksjon starter en for-løkke som
kjøres to ganger.

Første gangen den kjøres:
Vi setter en variabel c lik 2 og printer c, altså 2. Så sier vi at c skal være sin egen verdi pluss 1. Da blir
c = 3. Så opprettes en ny variabel b inne i funksjonen, den er altså lokal og overkjører ikke variabelen b fra
den andre funksjonen. Variabelen b tilordnes verdien 10. Så prøver programmet å sette b lik seg selv pluss a
men det er ingen global verdi a, så programmet kræsjer.

Andre gang i løkka kjøres ikke, da programmet kræsjer før dette. Men det ville foregått på helt lik måte som
første gangen løkka kjører. Etter hadde for-løkka tatt slutt, og vi ville gått tilbake til funksjonen
hovedprogram og resten av denne funksjonen. Hele programmet vil kræsje og resten av programmet kjøres aldri.
"""
