
def Verlorenagain():
  print("Je hebt verloren")
  c = input("Wil je nog een keer spelen (typ ja of nee) ")
  if c == "Ja" or c == "ja" or c == "JA":
    spel()
  else:
    print("GAME OVER")
    exit()

def Winagain():
    print("Je hebt gewonnen. Gefeliciteerd!")
    c = input("Wil je nog een keer spelen (typ ja of nee) ")
    if c == "Ja" or c == "ja" or c == "JA":
      spel()
    else:
      print("GAME OVER")
      exit()


kamers = {
  "padkeuze": {
    "title": "dit spel te laten beginnen",
    "beschrijving": "Je staat in de modder, met een grote heuvel voor je en een enorme schaduw hangt over je heen. Je denkt al jaren aan die ene legende die je hoorde van je opa. Eindelijk heb je je ouders kunnen overtuigen om je de reis naar de schat te laten gaan maken. De schat ligt op de berg. Je staat hier voor je eerste kruising. Je kan kiezen uit twee paden. Een lang en veilig pad of een kort en onveilig pad. Welk pad kies je?",
    "options": ["lang en veilig" , "kort en onveilig"],
    "lost": "nee",
    "win": "nee"
    },

  "kort en onveilig": { 
    "title": "een kort en onveilig pad",
    "beschrijving": "Je hebt een gewaagde keus gemaakt en kies voor het kort en onveilige pad. Echter is het pad zo onveilig dat je niet meer vooruit kan en niet meer achteruit. Het spel is over",
    "options": [""],
    "lost": "ja",
    "win": "nee",
    },
  "lang en veilig": {
    "title": "het lange en veilig pad",
    "beschrijving": "Je hebt het zekere voor het onzekere gekozen en gaat verder met je reis.  Op een moment voel je ineens de grond zacht worden en je begint weg te zakken!!! Oh nee!!! Je denkt aan het verhaal dat je opa je had verteld, het is drijfzand! Je kijkt op je heen en ziet de dingen waar je je mee kan redden. Een touw, een tak, heel lang nadenken", 
    "options": ["een touw", "een tak", "lang nadenken"],
    "lost": "no",
    "win": "no",
    },
  "lang nadenken": {
    "title": "heel lang nadenken",
    "beschrijving": "Na heel lang nadenken weet je het echt niet meer. Je zakt steeds verder in de modder. Nu kan je niet meer terug. De enige weg is terug naar huis. Je reis is helaas voorbij.",
    "options": [""],
    "lost": "ja",
    "win": "nee"
  },

  "een touw": {
    "title": "het touw om je te redden",
    "beschrijving": "Met behulp van het touw lukt het je om uit het drijfzand te komen. Je gaat verder met je reis. Na een paar uur lopen stoot je je voet ineens tegen iets hards! Je gaat kijken wat het is en ziet ineens een hamer uit de grond steken, dit moest vast van de ontdekkingsreizigers zijn die op zoek gingen naar de schat maar nooit meer waren teruggekomen! Zal je de hamer oppakken?.",
    "options": ["ja", "nee"],
    "lost": "no",
    "win": "no",
  },
  "een tak": {
    "title": "het tak om je te redden",
    "beschrijving": "Met behulp van het touw lukt het je om uit het drijfzand te komen. Je gaat verder met je reis. Na een paar uur lopen stoot je je voet ineens tegen iets hards! Je gaat kijken wat het is en ziet ineens een hamer uit de grond steken, dit moest vast van de ontdekkingsreizigers zijn die op zoek gingen naar de schat maar nooit meer waren teruggekomen! Zal je de hamer oppakken?.",
    "options": ["ja", "nee"],
    "lost": "no",
    "win": "no",
    },
} 



def Soortenkamers(kamer):
  huidigekamer = kamers[kamer] 
  titel = huidigekamer["title"]
  beschrijving = huidigekamer["beschrijving"]
  options = huidigekamer["options"]
  verliezen = huidigekamer["lost"]
  winnen = huidigekamer["win"]
  
  if verliezen == "ja":
    print(beschrijving)
    Verlorenagain()

  if winnen == "ja":
    print(beschrijving)
    Winagain()
    

  print (f"Je hebt gekozen voor {titel}.")
  print(beschrijving)
  print("Waarvoor kies je: ")
  print(" , ".join(options))

 
  VolgendeKamer = input()
  Soortenkamers(VolgendeKamer)   
  if VolgendeKamer == "q" or VolgendeKamer == "Q":
    Verlorenagain
  
  
def spel():
  a = input("Wat is je naam? ")
  print("Hallo " + a + ". Leuk dat je komt spelen, laten we beginnen!")
  print("Welkom bij de game je zal veel nieuwe ervaringen opdoen!")
  print("je kiest tussen (wind)richtingen, deze bestaan allemaal uit 1 letter.")
  print("Je mag zowel een hoofdletter als een kleine letter gebruiken.")
  print("Ook mag je op elk moment van het spel op de letter q drukken,dan zal het spel stoppen.")
  b = input("Heb je het begrepen? Typ ja of nee  ")
  if b == "nee" or b == "Nee":
    Verlorenagain()
  if b == "Ja" or b == "ja" or b == "JA": 
   Soortenkamers("padkeuze")
  if b == "q" or b == "Q":
    Verlorenagain()

spel()
  


