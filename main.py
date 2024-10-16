from random import randint, choice, randrange
from time import sleep
from os import system

#--the tank to act as a base and give alot of funtionality--
#___________________________________________________________


class Tank:
  def __init__(self, name):
    self.armour = 10
    self.power = 5
    self.alive = True
    self.name = name
    self.cost = 1000
    self.shot_count = 1
    self.miss_chance = 1
    
  #a funtion to make the tank handal the hit
  def takeDamage(self, damage):
    self.armour -= damage

    #cheeking if dead
    if self.armour <= 0:
      self.alive = False
    print(f"{self.name} has {self.armour} armour left")

  def splash(self, team, damige):
    other = get_tank_to_shot(team)
    if other == None:
      pass
    else:
      other.takeDamage(damige)
      print(f"The splash damange delt {damige} damage to {other.name}")

  #pinking a target and shouting
  def shot(self, enimy):
    other = get_tank_to_shot(enimy)

    #if there are no tanks to shot
    if other == None:
      print("Their all dead")

    #if the tank is alive it will shout
    elif self.alive:
      if randrange(1, 100) >= other.miss_chance:
        damige = randint(max(1, self.power//2), self.power)

        #pinting who is shouting ar who
        print(f"{self.name} is shoting {other.name} for {damige} damage")

        #appliying damige and diplating the other tanks remaing health
        other.takeDamage(damige)

        if other.armour <= -5:
          if other.armour <= -10:
            other.splash(enimy, 4)
            other.splash(enimy, 3)
          else:
            other.splash(enimy, 2)
      else:
        print(f"{self.name} has mised the {other.name}")
      
    #if the tank is dead it will not shot
    else:
      print(f"{self.name} is dead")
    
  #to show what the tank is and how dead it is
  def __str__(self):
    return f"{self.name}: {self.armour}HP\n"


#--------------------the types of units---------------------
#___________________________________________________________


class LightTank(Tank):

  def __init__(self, name):
    self.armour = 5
    self.power = 4
    self.alive = True
    self.name = name
    self.cost = 400
    self.shot_count = 1
    self.miss_chance = 20


class MediumTank(Tank):

  def __init__(self, name):
    self.armour = 10
    self.power = 5
    self.alive = True
    self.name = name
    self.cost = 700
    self.shot_count = 1
    self.miss_chance = 20
    

class HeavyTank(Tank):

  def __init__(self, name):
    self.armour = 17
    self.power = 6
    self.alive = True
    self.name = name
    self.cost = 1000
    self.shot_count = 1
    self.miss_chance = 10

  
class SuperHeavyTank(Tank):
  
  def __init__(self, name):
    self.armour = 21
    self.power = 6
    self.alive = True
    self.name = name
    self.cost = 1200
    self.shot_count = 1
    self.miss_chance = 5


class Tank_hunter(Tank):
  
  def __init__(self, name):
    self.armour = 7
    self.power = 16
    self.alive = True
    self.name = name
    self.cost = 1000
    self.shot_count = 1
    self.miss_chance = 20


class Tank_destroyer(Tank):
  
  def __init__(self, name):
    self.armour = 6
    self.power = 20
    self.alive = True
    self.name = name
    self.cost = 1200
    self.shot_count = 1
    self.miss_chance = 20


class Infitry(Tank):

  def __init__(self, name):
    self.armour = 1
    self.power = 2
    self.alive = True
    self.name = name
    self.cost = 120
    self.shot_count = 1
    self.miss_chance = 30


class AT_infintry(Tank):
  
  def __init__(self, name):
    self.armour = 1
    self.power = 10
    self.alive = True
    self.name = name
    self.cost = 200
    self.shot_count = 1
    self.miss_chance = 20


class Mortor_team(Tank):
  
  def __init__(self, name):
    self.armour = 1
    self.power = 7
    self.alive = True
    self.name = name
    self.cost = 600
    self.shot_count = 2
    self.miss_chance = 20
      

class BTR(Tank):

  def __init__(self, name):
    self.armour = 2
    self.power = 1
    self.alive = True
    self.name = name
    self.cost = 500
    self.shot_count = 5
    self.miss_chance = 30


class Decoy(Tank):

  def __init__(self, name):
    self.armour = 1
    self.power = 0
    self.alive = True
    self.name = name
    self.cost = 40
    self.shot_count = 0
    self.miss_chance = 1
  
#----------------------usefull funtions---------------------
#___________________________________________________________


def display_tanks():
  tank_types = [
    LightTank, MediumTank, 
    HeavyTank, SuperHeavyTank, 
    Tank_hunter, Tank_destroyer,
    Infitry, AT_infintry, Mortor_team,
    BTR, Decoy
  ]
  for t in tank_types:
    type = t(f"{t.__name__}")
    print(f"""{type}
    -  £{type.cost} 
    -  num shots : {type.shot_count}
    -  max damige {type.power} min damige {min(type.power//2+1, type.power)}
    -  other tanks have a {type.miss_chance}% chanes to miss\n""")

#___________________

#geting a living tank to shot "t
def get_tank_to_shot(tank_list):
  #removing dead tanks
  tank_list = [tank for tank in tank_list if tank.alive]

  #if there are no enimys left
  if len(tank_list) == 0:
    return None
  
  tank_to_shot = choice(tank_list)

  #geting a living tank in cases the preveas funtion did not work
  while not tank_to_shot.alive:
    tank_to_shot = choice(tank_list)
  
  return tank_to_shot

#___________________

def make_armada(name: str, money=3000):
  #the tanks in the armada and types of tanks thay can choues from
  tank_list = []
  tank_types = [
    LightTank, MediumTank, 
    HeavyTank, SuperHeavyTank, 
    Tank_hunter, Tank_destroyer,
    Infitry, AT_infintry, Mortor_team,
    BTR, Decoy
  ]

  #looing intill there is no money left
  while money > 0:
    #making a randm tank
    ran_type = choice(tank_types)
    tank = ran_type(name + " " + ran_type.__name__)

    #callculating if the tank is affordable or if there is not enogh money of any more units
    if money < 40:
      return tank_list
    elif tank.cost > money:
      continue
    else:
      tank_list.append(tank)
      money -= tank.cost
  return tank_list

#___________________

def check_player_inp(inp: str):
  tank_types = {
    LightTank : ["Light"], MediumTank : ["Mid"], 
    HeavyTank : ["Heavy"], 
    SuperHeavyTank : ["Supheavy", "Superheavytank", "Super Heavy Tank", "Super", "Sup"], 
    Tank_hunter : ["Hunt", "Hunter", "Tank_Hunter", "Tank Hunter"], 
    Tank_destroyer : ["Dest", "Tank_Destroyer", "Tank Destroyer"],
    Infitry : ["Inf", "Infitry"], AT_infintry : ["At Inf", "AT_Infintry", "At Infintry"],
    Mortor_team : ["Mort", "Mortor", "Mortor Team", "Mortor_Team"],
    BTR : ["Btr"], Decoy : ["Decoy", "Dec"]
  }

  amount = 1
  amount_inp = inp.split()[-1]
  if amount_inp.isnumeric():
    amount = max(1, int(amount_inp))
    inp = " ".join(inp.split()[:-1])

  
  for k, i in tank_types.items():
    if inp in i:
      return k, amount
  
  return None, amount

#___________________

def player_armada(name: str, money=3000):
  #the tanks in the armada and types of tanks thay can choues from
  tank_list = []

  display_tanks()

  print(f"You have {money} money")

  inp = input("Select the tank to go first: ").title().strip()

  while money > 0 and inp != "Break":
    t_type, amount = check_player_inp(inp)

    if t_type == None:
      print("that is not a tank")
      
    else:
      tank = t_type(name + " " + t_type.__name__)
      
      if (tank.cost * amount) > money:
        print("you do not have enough money for that tank")
      else:
        for r in range(amount):
          money -= tank.cost
          tank_list.append(tank)
        print(f"you have {money} money left")
        
        if money < 40:
          break
          
    inp = input("select the tank to go next: ").title().strip()

  system("clear")
  return tank_list

#-------------------------starting--------------------------
#___________________________________________________________

#atablishing the teams
team_1_name = "NATO"
team_2_name = "USA"

tanks_t1 = player_armada(team_1_name, 2400)
tanks_t2 = make_armada(team_2_name, 1500)

tanks_t1.sort(key=lambda x: (x.power * x.shot_count), reverse=True)
tanks_t2.sort(key=lambda x: (x.power * x.shot_count), reverse=True)

[print(t) for t in tanks_t1]
print("-------------------")
[print(t) for t in tanks_t2]

print("-------------------")
print(f"Team {team_1_name} has {len(tanks_t1)} Units")
print(f"Team {team_2_name} has {len(tanks_t2)} Units")
input()
print("-------------------")


#-------------------------fighting--------------------------
#___________________________________________________________


while len(tanks_t1) > 0 and len(tanks_t2) > 0:
  for tank in range(max(len(tanks_t1), len(tanks_t2))):
    
    if not (tank > len(tanks_t1) - 1):
      print("\033[1;39m")
      print(f"{team_1_name} turn:")

      if tanks_t1[tank].shot_count > 0:
        for i in range(tanks_t1[tank].shot_count):
          tanks_t1[tank].shot(tanks_t2)
          print()
      else:
        print("It's a decoy")
        
      sleep(0.05)
    
    #___________________
    
    if not (tank > len(tanks_t2) - 1):
      print("\033[1;30m")
      print(f"{team_2_name} turn:")
      
      if tanks_t2[tank].shot_count > 0:
        for i in range(tanks_t2[tank].shot_count):
          tanks_t2[tank].shot(tanks_t1)
          print()

      else:
        print("It's a decoy")
      sleep(0.05)

  tanks_t1 = [tank for tank in tanks_t1 if tank.alive]
  tanks_t2 = [tank for tank in tanks_t2 if tank.alive]

  #___________________

  print("\033[1;39m")
  print(f"{team_1_name} remaing uinits:")
  [print(t) for t in tanks_t1]
  
  print("\033[1;30m")
  print(f"{team_2_name} remaing uinits:")
  [print(t) for t in tanks_t2]

  print("-------------------")
    
  sleep(1)

  print("\n")

#---------------------win condishon-------------------------
#___________________________________________________________

print("\x1b[21;44;38m")

tanks_t1 = [tank for tank in tanks_t1 if tank.alive]
tanks_t2 = [tank for tank in tanks_t2 if tank.alive]

if len(tanks_t1) > 0:
  print(f"{team_1_name} is the winner with {len(tanks_t1)} units left")
  [print(t) for t in tanks_t1]

else:
  print(f"{team_2_name} is the winner with {len(tanks_t2)} units left\n")
  [print(t) for t in tanks_t2]

print("\n\n\n")
