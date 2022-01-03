from dinosaur import Dinosaur
#here i will create the dinosaurs to put in the herd
class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    
    def create_herd(self):
        dino_one = Dinosaur('Triceratops', 20)
        dino_two = Dinosaur('Ankylosaurus', 25)
        dino_three = Dinosaur('Velociraptor', 15)

        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
    
