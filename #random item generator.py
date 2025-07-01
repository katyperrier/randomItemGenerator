import random as r


#random item generator
#proof of concept

# [Adjective] [Item] of [Substance]

adjective = ["Molten","Radiant","Gloomy","Ancient","Arcane","Venomous"
             ,"Heaven-forged","Hell-forged","Jewel-encrusted","Permafrosted"
             ,"Electric","Singing","Whistling","Humming","Crescent"]
item = ["Sword","Axe","Helmet","Spear","Gauntlet","Lance"]
substance = ["Fire","Ice","Lightning","Magic","Song"]

selectedAdjective = adjective[r.randint(0,4)]

print(selectedAdjective)
