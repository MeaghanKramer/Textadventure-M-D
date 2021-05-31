import time
def again():
  print("Je hebt verloren")
  c = input("Wil je nog een keer spelen (typ ja of nee) ")
  if c == "Ja" or c == "ja":
    spel()
  else:
    exit() 

kamers = {
  "padkeuze": {
    "title": "padkeuze",
    "beschrijving": "Je staat in de modder, met een grote heuvel voor je en een enorme schaduw hangt over je heen. Je denkt al jaren aan die ene legende die je toen hoorde van je opa. Eindelijk heb je je ouders kunnen overtuigen om je op reis te laten gaan en je gaat op zoek naar de schat waar je opa je zoveel verhalen over had verteld. De schat ligt op de berg. Je staat hier voor je eerste kruising, welk pad zal je kiezen?",

    "options": ["modder" , "padkeuze"]
    },

  "modder": { 
    "title": "modder",
    "beschrijving": "Je hebt de lange weg gekozen en gaat op pad. Er is nu geen weg meer terug! Je loopt verder op het pad en voelt ineens de grond zacht worden en je begint weg te zakken!!! Oh nee!!! Je denkt aan het verhaal dat je opa je had verteld, het is drijfzand! Je kijkt op je heen en ziet de dingen waar je je mee kan redden",
  } 
} 

def Soortenkamers(kamer):
  huidigekammer = kamers[kamer] 
  title = huidigekammer["title"]
  beschrijving = huidigekammer["beschrijving"]
  print (f"Je bent nu in de {title}.")
  print(beschrijving)
  print("Welke pad kies je nu: ")
  print(" , ".join(kamers.keys()))

  VolgendeKamer = input()
  Soortenkamers(VolgendeKamer)   


def spel():
  a = input("Wat is je naam? ")
  print("Hallo " + a + ". Leuk dat je komt spelen, laten we beginnen!")
  time.sleep(2)
  print("Welkom bij de game je zal veel nieuwe ervaringen opdoen!")
  time.sleep(1)
  print("je kiest tussen (wind)richtingen, deze bestaan allemaal uit 1 letter.")
  time.sleep(1)
  print("Je mag zowel een hoofdletter als een kleine letter gebruiken.")
  time.sleep(1)
  print("Ook mag je op elk moment van het spel op de letter q drukken,dan zal het spel stoppen.")
  time.sleep(2)
  b = input("Heb je het begrepen? Typ ja of nee  ")
  if b == "nee" or b == "Nee":
    again()
  if b == "Ja" or b == "ja": 
   Soortenkamers("padkeuze")

spel()
  


