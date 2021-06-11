import os
from kamer import kamers
from time import sleep

#code voor loading screen
def progress(percent=0, width=30):
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

print('This will take a moment')
for i in range(101):
    progress(i)
    sleep(0.05)
print()
# eind code loading screen

#begin code, uit functie zodat er naar de naam verwezen kan worden bij game over en winst

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

#Als de speler heeft verloren treedt dit in werking

def nogmaals() :
    os.system("clear")
    m = input("Je hebt niet tussen ja en nee gekozen, maak aub de keuze opnieuw... Misschien vrrlies je eze keer niet? :) Kies je ja of nee?")
    if m == "nee" or m == "Nee":
      exit()
    if m == "Ja" or m == "JA" or m == "ja":
      spel()
    else:
      nogmaals()
    nogmaals()

def Verlorenagain():
  print ("-" * 80)
  print("Helaas heb je verloren... Om heel eerlijk te zijn had ik wel beter van jou verwacht," + a + " " + d + ",volgende keer beter dan maar!")
  print("-" * 80)
  c = input("Wil je nog een keer spelen (typ ja of nee) ")
  print("-" * 80)
  if c == "Ja"or c == "ja" or c == "JA" :
    spel()
  if c == "nee" or c == "NEE" or c == "Nee":
    print ("Jammer, tot de volgende keer!")
    exit()
  else:
    nogmaals()
  Verlorenagain()


def Winagain():
    print("JE ZIET DE SCHAT LIGGEN!!! JAAA!!! Gefeliciteerd," + a + " " + d + ", je hebt gewonnen!")
    c = input("Wil je nog een keer spelen (typ ja of nee) ")
    if c == "Ja" or c == "ja" or c == "JA":
      spel()
    else:
      print("GAME OVER, maar je hebt tenminste gewonnen :)")
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
  


