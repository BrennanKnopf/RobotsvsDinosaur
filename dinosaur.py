import time
class Dinosaur: #the dinosaurs need to be established with what kind they are, their health, their attack power, their engergy and the type of attack they will use
    def __init__(self, kind, attack_damage):
        self.kind = kind
        self.health = 100
        self.attack_damage = attack_damage
        self.energy = 100
        self.attack_type = ('bite', 'tail smash', 'headbutt')
    
    def attack_robot(self, robot_attacked):
        if self.energy > 10:
           attack_choice = int(input(f'Choose what Dinosaur to attack with: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, (3) {self.attack_type[2]}.')) 
        for attack in range(attack_choice):
            time.sleep(1)
            if attack_choice == 1:
               print(f'{self.kind} attacked {robot_attacked.name} with {self.attack_type[0]} doing {self.attack_damage} damage.')
               break
            elif attack_choice == 2:
                print(f'{self.kind} attacked {robot_attacked.name} with {self.attack_type[1]} doing {self.attack_damage} damage.')
                break
            elif attack_choice == 3:
                print(f'{self.kind} attacked {robot_attacked.name} with {self.attack_type[2]} doing {self.attack_damage} damage.')
                break
            
    
        self.energy -= 10
        robot_attacked.health -= self.attack_damage
        print(f'{self.kind} energy is now {self.energy}')
        time.sleep(1)
        print(f'{robot_attacked.name} health is now {robot_attacked.health}')

