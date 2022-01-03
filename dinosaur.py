class Dinosaur: #the dinosaurs need to be established with what kind they are, their health, their attack power, their engergy and the type of attack they will use
    def __init__(self, kind, attack_power):
        self.kind = kind
        self.health = 100
        self.attack_power = attack_power
        self.energy = 100
        self.attack_type = ('bite', 'tail smash', 'headbutt')
    
    def dino_attack(self, robot_attacked):
        if self.energy > 10:
           attack_choice = int(input(f'Choose what Dinosaur to attack with: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, (3) {self.attack_type[2]}.')) 
        for attack in attack_choice:
            if attack_choice == 1:
               print(f'{self.kind} attacked {robot_attacked.name} with {self.attack_type[0]}')
            elif attack_choice == 2:
                print(f'{self.kind} attacked {robot_attacked.name} with {self.attack_type[1]}')
            elif attack_choice == 3:
                print(f'{self.kind} attacked {robot_attacked.name} with {self.attack_type[3]} ')
            
    
        self.energy -= 10
        robot_attacked.health -= self.attack_power
        print(f'{self.kind} energy is now {self.energy}')
        print(f'{robot_attacked.name} health is now {robot_attacked.health}')

