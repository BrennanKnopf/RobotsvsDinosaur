from robot import Robot
from weapon import Weapon
#Here i will establish a fleet, by creating the instance of the weapons and robots themselves.
class Fleet:
    def __init__(self):
        self.storage = []
        self.create_fleet()
    
    def create_fleet(self):
        weapon_one = Weapon('shovel', 10)
        weapon_two = Weapon('gun', 25)
        weapon_three = Weapon('grenade', 50)

        first_robot = Robot('Wall-E', weapon_one)
        second_robot = Robot('Chappie', weapon_two)
        third_robot = Robot('Sonny', weapon_three)