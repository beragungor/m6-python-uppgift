Projektförslag - Måns, Ahmet - “Bikeability” 

Vår idé
Våran idé går ut på att skapa en algoritm, som avgör om det är rimligt att ta cykeln idag eller inte beroende på temperatur, vind, luftfuktighet och nederbörd. 
Problemet som löses är alltså det när personer cyklar till exempelvis universitet eller jobb trots tuffa väderförhållanden som kan leda till olyckor. Med hjälp av systemet kan personer ta en snabb titt i appen som avgör om man bör undvika cykeln idag eller inte.
Därför är det intressant för andra personer förutom oss själva som cyklar eftersom det är så många i Uppsala som cyklar.

Systemets delar
Systemet kan brytas ned i flera mindre delar. Vi behöver en fil eller funktion som tar väderdata från en databas, en funktion för varje variabel vi undersöker, en algoritm som tar dessa variabler och med hjälp av logik avgör om det är okej att ta cykeln, samt något som frågar om staden för att få koordinaterna till dessa.

Temperatur representeras av en string ("X °C)
Vind represnteras av en string ("X m/s)
Relativ luftfuktighet (RH) representeras av en string ("X %)
Nederbörd representeras av en string ("X mm)

Användaren kommer bli frågad vilken stad hen vill kolla vädret, så koordinaterna kommer att tas från denna stad och representeras av en float, t.ex. (59.8586, 17.6389)

Koordinaterna kommer ta vädret för denna plats och ge värdena för variablerna.
Alla data skulle kunna vara i en dictionary, så vi har namn på staden, sen t.ex. "nederbörd" : "x mm" osv.

Komplexitet och förenkling
Vi skulle kunna börja med bara vindhastighet, alltså en variabel eller två, och sen utöka om tid finns.

En annan förenkling med koordinaterna skulle kunna vara att det är bara temperaturen i Uppsala som mäts, eller att användaren måste själv skriva in koordinaterna för staden.
Sen behöver vi inte till en början ha en interface med pygame, utan det skulle funka om det bara körs i terminalen.

Om vi skulle vilja göra projektet mer komplicerat skulle output kunna vara mer än bara jag eller nej, man skulle kunna ha exempelvis att det är okej att cykla, eller att det går ganska bra/dåligt. 

Prognosen skulle kunna vara med, så man kan skriva in tiden för när man ska cykla, och kolla om det är okej att cykla då. 

Ifall allt detta hinns med skulle man även kunna ha med personens destination, så ifall man inte kan cykla kan man ge t.ex. förslag på buss, och ger då bussnummer och när de avgår. 


Personliga utvecklingsmål
Våra personliga utvecklingsmål kommer att ta hänsyn på det sätt att vi har ganska liknande mål. Vi båda vill bli bättre på att använda dictionaries samt att kunna ta data från internet/databaser och implementera det till koden. Jag, Måns, vill gärna även lära mig använda 2d-listor, och det kommer vi antagligen att få ihop på något sätt om vi ska köra programmet i terminalen.


