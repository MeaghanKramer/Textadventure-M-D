import os
from kamer import kamers
from time import sleep

def progress(percent=0, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

print('This will take a moment')
for i in range(101):
    progress(i)
    sleep(0.05)
print()

os.system("clear")
print("Laten we beginnen!")
print("-" * 80)
a = input("Wat is je naam? ")
d = input("En wat is je achternaam? ")
os.system("clear")
print ("-" * 80)
print("Hallo " + a + " " +  d + ". Leuk dat je komt spelen, laten we beginnen!")
print("Welkom bij de game je zal veel nieuwe ervaringen opdoen!")
print("je kiest tussen (wind)richtingen, deze bestaan allemaal uit 1 letter.")
print("Je mag zowel een hoofdletter als een kleine letter gebruiken.")
print("Ook mag je op elk moment van het spel op de letter q drukken,dan zal het spel stoppen.")
print('-' * 80)

inventory = []

def Verlorenagain():
  print("Helaas heb je verloren... Om heel eerlijk te zijn had ik wel beter van jou verwacht," + a + " " + d + ",volgende keer beter dan maar!")
  c = input("Wil je nog een keer spelen (typ ja of nee) ")
  if c == "Ja" or c == "ja" or c == "JA":
    spel()
  else:
    print("GAME OVER")
    exit()

def Winagain():
    print("JE ZIET DE SCHAT LIGGEN!!! JAAA!!! Gefeliciteerd," + a + " " + d + ", je hebt gewonnen!")
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
    os.system('clear')
    print("-" * 80)
    print(beschrijving)
    print("-" * 80)
    Verlorenagain()

  if winnen == "ja":
    os.system('clear')
    print("-" * 80)
    print(beschrijving)
    print("-" * 80)
    Winagain()
    
  os.system('clear')
  print('-' * 80)
  print (f"Je hebt gekozen voor {titel}.")
  print(beschrijving)
  print("Waarvoor kies je: ")
  print(", ".join(options))
  print("-" * 80)
  
  def invoeren():
    Volgende = input('')
    if Volgende.lower() in options:
      Soortenkamers(Volgende)
    elif Volgende.lower() == "q":
      Verlorenagain()
    else:    
      os.system("clear")
      print("Je hebt het verkeerde ingetypt")
      print ("Weet je zeker dat je geen spatie teveel hebt?")
      print("kies nogmaals uit deze keuzes")
      print(" , ".join(options))
      print ("-" * 80)
      invoeren()

  invoeren()
  

def spel():
 
  def Begrepen():
    b = input("Heb je het begrepen? Typ ja of nee  ")
    if b == "nee" or b == "Nee":
     Verlorenagain()
    if b == "Ja" or b == "ja" or b == "JA": 
      Soortenkamers("padkeuze")
    if b == "q" or b == "Q":
       Verlorenagain()
    else:
      print("je hebt een niet geldige keuze ingevoerd.")
      Begrepen()
  Begrepen()

spel()
  


