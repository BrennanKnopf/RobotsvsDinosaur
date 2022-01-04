from robot import Robot
from weapon import Weapon
#Here i will establish a fleet, by creating the instance of the weapons and robots themselves.
class Fleet:
    def __init__(self):
        self.robots = []
        self.weapon_choice = [Weapon('shovel', 10), Weapon('gun', 25), Weapon('grenade', 50) ] #turning the objects into a list allows for the robots to be able to choose one weapon without carrying all the weapons
        self.create_fleet()
        
    
    def create_fleet(self):
        
        equipped_weapon1 = self.weapon_selection()
        equipped_weapon2 = self.weapon_selection()
        equipped_weapon3 = self.weapon_selection()
        first_robot = Robot('Wall-E', self.weapon_choice[equipped_weapon1]) #equips the weapons chosen for the robots at the beginning of the game.
        second_robot = Robot('Chappie', self.weapon_choice[equipped_weapon2])
        third_robot = Robot('Sonny', self.weapon_choice[equipped_weapon3])

        self.robots.append(first_robot)
        self.robots.append(second_robot)
        self.robots.append(third_robot)

    def weapon_selection(self):
        print('Choose your weapons.')
        weapon_options = ('press (1) for shovel\n'
                            'press (2) for gun\n'
                            'press (3) for grenade\n')
        choice = input(weapon_options)
        return int(choice) - 1
    
    