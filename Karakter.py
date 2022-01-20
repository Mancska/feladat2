import random
Classlist = ["Artificer", "Barbarian", "Bard"," Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer","Warlock","Wizard"]
kaszt=str(Classlist)
print("elérhetö kasztok: "+(kaszt.replace("[","").replace("]","")))

kasztValaszt=""

lista1=[]
def Valasztas():
  kasztValaszt = input("A választot kasztod gépeld be ide: ")
  if kasztValaszt in Classlist:
    lista1.append(kasztValaszt)
  else:
    Valasztas()

Valasztas()

Racelist = ["Dragonborn","Dwarf","Elf","Gnome","Half-Elf","Halfling","Half-Orc","Human","Tiefling"]
faj=str(Racelist)
print("Választható fajok: "+(faj.replace("[","").replace("]","")))

lista2=[]
fajvalaszt=""
def Valasztas2():
  fajvalaszt= input("A választot fajod gépeld be ide: ")
  if fajvalaszt in Racelist:
    lista2.append(fajvalaszt)
  else:
    Valasztas2()

Valasztas2()

abbilitylist = ["Strength","Constitution","Dexterity","Intelligence","Wisdom","Charisma"]

def dobas ():
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  roll3 = random.randint(1, 6)
  roll4 = random.randint(1, 6)
  mylist = [roll1,roll2,roll3,roll4]
  mylist.remove(min(mylist))
  ertek = sum(mylist)
  return  ertek


ertekOsztas=[]
for i in range(6):
  szam=dobas()
  ertekOsztas.append(szam)
ertek=str(ertekOsztas)
print("tulajdonságok ki dobása: "+ertek)
print("a fönt ki dobott számokat most majd osszd szét a tulajdonságaidon: ")
Strength =int(input("adja meg az értékét: "))
Constitution = int(input("adja meg az értékét: "))
Dexterity = int(input("adja meg az értékét: "))
Intelligence = int(input("adja meg az értékét: "))
Wisdom = int(input("adja meg az értékét: "))
Charisma= int(input("adja meg az értékét: "))


#faji bonuszok
if fajvalaszt == ["Dragonborn"]:
  Strength += 2
  Charisma += 1
if fajvalaszt == ["Dwarf"]:
  Constitution += 2
if fajvalaszt == ["Elf"]:
  Dexterity += 2
if fajvalaszt == ["Gnome"]:
  Intelligence += 2
if fajvalaszt == ["Half-Elf"]:
  Charisma += 2
if fajvalaszt == ["Halfling"]:
  Dexterity += 2
if fajvalaszt == ["Half-Orc"]:
  Strength += 2
  Constitution += 1
if fajvalaszt == ["Human"]:
  Strength += 1
  Constitution += 1
  Dexterity += 1
  Intelligence += 1
  Wisdom += 1
  Charisma += 1
if fajvalaszt == ["Tiefling"]:
  Charisma += 2
  Intelligence += 1

def modosit(fname):
  mod1=0
  if fname == 0 or fname == 1:
      mod1 = -5
  if fname == 2 or fname == 3:
      mod1 = -4
  if fname == 4 or fname == 5:
      mod1 = -3
  if fname == 6 or fname == 7:
      mod1 = -2
  if fname == 8 or fname == 9:
      mod1 = -1
  if fname == 10 or fname == 11:
      mod1 = 0
  if fname == 12 or fname == 13:
      mod1 = 1
  if fname == 14 or fname == 15:
      mod1 = 2
  if fname == 16 or fname == 17:
      mod1 = 3
  if fname == 18 or fname == 19:
      mod1 = 4
  if fname == 20 or fname == 21:
      mod1 = 5
  fname = mod1
  return fname

print("======================================")
print("Race:","".join(lista2))
print("Class","".join(lista1))


#ki iratás
print("======================================")
print("-Strength",Strength)
print("-Constitution",Constitution)
print("-Dexterity",Dexterity)
print("-Intelligence",Intelligence)
print("-Wisdom",Wisdom)
print("-Charisma",Charisma)

#érték adás
print("======================================")
print("Strength modositó:",modosit(Strength))
print("Constitution modositó:",modosit(Constitution))
print("Dexterity modositó:",modosit(Dexterity))
print("Intelligence modositó:",modosit(Intelligence))
print("Wisdom modositó:",modosit(Wisdom))
print("Charisma modositó:",modosit(Charisma))
print("======================================")

