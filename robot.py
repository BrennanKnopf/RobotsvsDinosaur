from weapon import Weapon
import time
#The robots need a name, health level, they will use a weapon, so i need a list of weapons to choose from
class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.weapon = weapon
       
        
    def attack_dinosaur(self, dinosaur_attacked):
        while self.power_level > 10:
            time.sleep(1)
            print(f'{self.name} attacked {dinosaur_attacked.kind} with {self.weapon.name} doing {self.weapon.attack_power} damage.')
            break

           

        self.power_level -= 10
        dinosaur_attacked.health -= self.weapon.attack_power
        print(f'{self.name} energy level is now {self.power_level}')
        time.sleep(1) 
        print(f'{dinosaur_attacked.kind} health is now {dinosaur_attacked.health}')       





