import random
import time
import json
import os

filename = "/storage/emulated/0/Py_Test/Improving/data.json"
game = True
coin = 0
inventory = {}
equip_item = {}
role = {}
item_effect = {}
skills = {}
chestprice = {
  'ChestNormal' : 28,
  'ChestRare' : 36,
  'ChestHidden' : 73
}


def normal_chest():
  """Gives an item"""
  global coin
  coin += 1
  if "leather" not in inventory.keys():
    inventory['leather'] = 1
  else:
    inventory['leather'] += 1
  save()

def rare_chest():
  """Gives an item"""
  global coin
  coin += 10
  if "dagger" not in inventory.keys():
    inventory['dagger'] = 1
  else:
    inventory['dagger'] += 1
  save()

def heaven_chest():
  """Gives an item"""
  global coin
  coin += 20
  if "armor" not in inventory.keys():
    inventory['armor'] = 1
  else:
    inventory['armor'] += 1
  if "dagger" not in inventory.keys():
    inventory['dagger'] = 1
  else:
    inventory['dagger'] +=1
  save()
    

def SellHidden():
    global coin
    hidden = chestprice['ChestHidden']
    coin += hidden
    print(f"You Sell Hidden Chest For {hidden}")
    save()


def SellRare():
    global coin
    rare = chestprice['ChestRare']
    coin += rare
    print(f"You Sell Rare Chest For {rare}")
    save()
    
    
def SellNormal():
    global coin
    norm = chestprice['ChestNormal']
    coin += norm
    print(f"You Sell Normal Chest For {norm}")
    save()
    
    
def equip():
  """Let You Equip An Item"""
  equip = input("Equip An Item")
  invalid = ['leather','coin']
  
  if equip in inventory.keys() and equip not in invalid:
    if equip in equip_item:
      print("You Already Equip This Item..Baka")
    else:
      equip_item.append(equip)
      if inventory[equip] < 2:
        del inventory[equip]
      else:
        inventory[equip] -= 1
  
  elif equip not in inventory.keys():
    print("You Don't Have This Item")
  elif equip in invalid:
    print("You Can't Equip This Item")


def eq():
  """check's your equip item"""
  for i in equip_item:
    print(i)


def Coins():
    print(f"--Silver Coin--\n{coin.center(10)}")


def check():
  """check the inventory"""
  print("--inventory--".center(10))
  for k,v in inventory.items():
    print(f"-{k}\t{v}".center(10))


def load():
    """Load The Progress"""
    global coin
    global filename

    try:
      with open(filename) as loads:
        data = json.load(loads)
        item = data['player']['inventory']
        money = data['player']['money']
        
        coin += int(money)
        
        for items,value in item.items():
          inventory[items] = value

    except FileNotFoundError:
        with open(filename,"w") as f:
          user = {
          'player' : {'inventory' : {}, 'money' : 0 }
          }
          json.dump(user,f, indent=4)

def save():
    """Save The Progress"""
    global coin
    global filename

    try:
      with open(filename,'r') as f:
          data = json.load(f)
          items = data['player']['inventory']
          data['player']['money'] = coin
      with open(filename,'w') as wr:
        for item,value in inventory.items():
            items[item] = value
        json.dump(data,wr,indent=4)
    except FileNotFoundError:
      with open(filename,'w') as new:
        user = {
          'player' : {'inventory' : {}, 'money' : 0 }
        }
        json.dump(user,new, indent=4)
      save()
            

while game:
  if len(inventory) < 1 or coin < 1:
    load()
    
  say = input("Do You Want To Explore The Heaven' Land?\n").lower()
  answers = ['open','o']
  answersell = ['sell','s']
  if say == "yes" or say == "y":
    chest1 = ["Normal Chest","Heaven Chest","Rare Chest"]
    chest2 = random.choice(chest1)
    if chest2 == chest1[0]:
      print("You Found A Normal Chest")
      Normal_Chest = True
      while Normal_Chest:
          question = input("Open/Sell:\n").lower()
          if question in answers:
              normal_chest()
              Normal_Chest = False
          elif question in answersell:
              SellNormal()
              Normal_Chest = False
      continue
    elif chest2 == chest1[1]:
      print("You Found A Hidden Chest")
      Hidden_Chest = True
      while Hidden_Chest:
          question = input("Open/Sell:\n").lower()
          if question in answers:
              heaven_chest()
              Hidden_Chest = False
          elif question in answersell:
              SellHidden()
              Hidden_Chest = False
      continue
    elif chest2 == chest1[2]:
      print("You Found A Rare Chest")
      Rare_Chest = True
      while Rare_Chest:
          question = input("Open/Sell:\n").lower()
          if question in answers:
              rare_chest()
              Rare_Chest = False
          elif question in answersell:
              SellRare()
              Rare_Chest = False
    continue
  elif say == "inv":
    check()
  elif say == "equip":
    equip()
  elif say == "items":
    eq()
  elif say == "skill":
    skill()
  elif say == "coin":
      Coins()
  elif say == "q":
      save()
      game = False