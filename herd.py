from dinosaur import Dinosaur
#here i will create the dinosaurs to put in the herd
class Herd:
    def __init__(self):
        self.dinosaur = []
        self.create_herd()
    
    def create_herd(self):
        dino_one = Dinosaur('Triceratops', 20)
        dino_two = Dinosaur('Ankylosaurus', 25)
        dino_three = Dinosaur('Velociraptor', 15)

        self.dinosaur.append(dino_one)
        self.dinosaur.append(dino_two)
        self.dinosaur.append(dino_three)
    
