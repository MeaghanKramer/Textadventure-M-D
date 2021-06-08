import os

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
  "nee": {
    "title": "de hamer niet op te pakken",
    "beschrijving": "je bent net de pijn uit je voet kwijt als je ineens een raar figuur in de verte ziet staan, het lijkt op een bosbewoner! Hij komt op je af met een aardig snel tempo, oh nee wat nu?!!. Je kan de bosbewoner uitschelden, begroeten, of negeren",
    "options": ["begroeten", "negeren", "uitschelden"],
    "lost": "no",
    "win": "no",
    },
  "begroeten": {
    "title": "om rustig te blijven en het wezen te begroeten",
    "beschrijving": "je besluit toch maar even de kaart van je opa te bekijken, je bent al over de helft van de route naar de schat! Je ziet ineens de bloedvlekken op de kaart die je eerder nog niet zijn ogevallen, je hoort gegrom boven je en kijkte omhoog, het is een woeste Dodo! Maar die waren toch uitgestorven, hier niet! Wat doe je? dood maken of rustig blijven",
    "options": ["dood maken", "rustig blijven"],
    "lost": "no",
    "win": "no"
    }
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
    
  os.system('clear')
  print('-' * 80)
  print (f"Je hebt gekozen voor {titel}.")
  print(beschrijving)
  print("Waarvoor kies je: ")
  print(" , ".join(options))
  print('-' * 80)

    
  
  Volgende = input()
  if Volgende == "q" or Volgende == "Q":
    Verlorenagain()
  elif not Volgende in options:    
    print("Je hebt het verkeerde ingetypt")
    print("kies nogmaals uit deze keuzes")
    print(" , ".join(options))
    Volgende = input()
    if not Volgende in options:    
      print("Je hebt het verkeerde ingetypt")
      print("kies nogmaals uit deze keuzes")
      print(" , ".join(options))
      Volgende = input()
      if not Volgende in options:  
        print("Je hebt het verkeerde ingetypt")
        print("kies nogmaals uit deze keuzes")
        print(" , ".join(options))
        Volgende = input()
        if not Volgende in options:
         print("je hebt meerdere malen het verkeerde ingetypt. Het spel houdt nu echt op")
         Verlorenagain()
    
  elif Volgende in options:
    Soortenkamers(Volgende)   


  
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
  


