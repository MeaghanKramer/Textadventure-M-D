import os
from kamer import kamers

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
  


