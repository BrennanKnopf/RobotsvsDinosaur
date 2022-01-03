from robot import Robot
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
import random



class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        self.display_welcome()
        self.team = self.choose_team()
        self.battle()
    
    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs.')
        print('Each team will start with 100 health.')
        print('Each team will also start with 100 energy')
        print('Every time you attack it will cost you 10 energy')
        print('The winner will be decided when all opponents have been defeated')
        print('Opponents are defeated when they reach 0 health')
        print('Choose which team you would like.')
        print('Good Luck')

    def choose_team(self):
        team_choice = int(input('Choose your team: (1) Robots; (2) Dinosaurs'))
        if team_choice == 1:
            print('You chose the fleet of Robots')
            return team_choice
        elif team_choice == 2:
            print('You chose the herd of Dinosaurs')
            return team_choice
        else:
            print('Invalid answer. Try again.')
            self.choose_team()


    def battle(self):
        first_turn = random.randit(1,2)
        if first_turn == 1:
            print('Robots are up first.')
            first_turn = 1
        elif first_turn == 2:
            print('Dinosaurs are up first.')
            first_turn = 2

       
           


        

    def dino_turn(self, dinosaur):
        self.show_dino_opponent_options()
        self.herd.dinosaur[0].attack_robot(self.fleet.robots[0])
        

    def robo_turn(self, robot):
        self.show_robot_opponent
        self.fleet.robot[0].attack_dinosaur(self.herd.dinosaurs[0])


    def show_dino_opponent_options(self):
       turn = 1
       for character in self.fleet.robot:
            print(f'{character.name} has {character.health} health.')
            turn += 1


    def show_robot_opponent_options(self):
        turn = 1
        for character in self.herd.dinosuar:
            print(f'{character.kind} has {character.health} health. ')
            turn += 1

    def display_winners(self):
        pass
    
        