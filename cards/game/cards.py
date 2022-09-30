import random

class Cards():
    
    def __init__(self):
       
        self.first_card = 0
        self.second_card = 0
        self.points = 0

    def draw(self):
        self.first_card = random.randint(1, 13)
        self.second_card = random.randint(1, 13)

    def get_points(self, guess):
        points = 0

        if ((guess == "l" and self.first_card > self.second_card) or
            (guess == "h" and self.first_card < self.second_card)):
            points = 100
        else:
            points = -75
        
        return points