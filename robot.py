from weapon import Weapon
#The robots need a name, health level, they will use a weapon, so i need a list of weapons to choose from
class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.energy_level = 100
        self.weapon = weapon
        self.weapon_choice = ['shovel', 'gun', 'grenade']

    weapon_one = Weapon('shovel', 10)
    weapon_two = Weapon('gun', 25)
    weapon_three = Weapon('grenade', 50) 
    
    
    def attack_dinosaur(self, dinosaur_attacked):
        if self.energy_level > 10:
            attack_choice = int(input(f'Choose what weapon to attack with: (1) {self.weapon_choice[0]}, (2) {self.weapon_choice[1]}, (3) {self.weapon_choice[2]}.'))
  
        for attack in range(attack_choice):
            if attack_choice == 1:
               print(f'{self.name} attacked {dinosaur_attacked.kind} with {self.weapon_choice[0]}')
               break
            elif attack_choice == 2:
                print(f'{self.name} attacked {dinosaur_attacked.kind} with {self.weapon_choice[1]}')
                break
            elif attack_choice == 3:
                print(f'{self.name} attacked {dinosaur_attacked.kind} with {self.weapon_choice[2]} ')
                break
        

        self.energy_level -= 10
        dinosaur_attacked.health -= self.weapon.attack_power
        print(f'{self.name} energy level is now {self.energy_level}') 
        print(f'{dinosaur_attacked.kind} health is now {dinosaur_attacked.health}')       





