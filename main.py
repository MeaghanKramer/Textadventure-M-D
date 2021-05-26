


def vragen():
  b = input("Heb je het begrepen? Typ ja of nee  ")
  if b == "Ja" or b == "ja": 
      print("Ja staat in de modder, met een grote heuvel voor je en een enorme schaduw hangt over je heen. Je denkt al jaren aan die ene legende die je toen hoorde van je opa. Eindelijk heb je je ouders kunnen overtuigen om je op reis te laten gaan en je gaat op zoek naar de schat waar je opa je zoveel verhalen over had verteld. De schat ligt op de berg. Je staat hier voor je eerste kruising, welk pad zal je kiezen?  ")
  elif b == "Nee" or b == "nee":
      print("Je bent dom, game over")
      print("Wil je nog een keer spelen?")
  else: 
    print("Je hbt het verkeerde ingetypt")
      


def spel():
  a = input("Wat is je naam? ")
  print("Hallo " + a + ". Leuk dat je komt spelen, laten we beginnen!")
  
  print("Welkom bij de game je zal veel nieuwe ervaringen opdoen! Tijdens het spel kan je kiezen tussen verschillende (wind)richtingen, deze zullen allemaal uit 1 letter bestaan. Je mag zowel een hoofdletter als een kleine letter gebruiken. Ook mag je op elk moment van het spel op de letter q drukken, dan zal het spel stoppen.")

  vragen()
  



spel()
  


