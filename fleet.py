from robot import Robot
from weapon import Weapon
#Here i will establish a fleet, by creating the instance of the weapons and robots themselves.
class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
      
        first_robot = Robot('Wall-E', Weapon)
        second_robot = Robot('Chappie', Weapon)
        third_robot = Robot('Sonny', Weapon)

        self.robots.append(first_robot)
        self.robots.append(second_robot)
        self.robots.append(third_robot)
    