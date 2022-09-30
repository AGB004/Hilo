import random

class Cards():
    
    def __init__(self):
       
        self.first_card = 0
        self.second_card = 0
        self.points = 0

    def draw(self):
        self.first_card = random.randint(1, 13)
        self.second_card = random.randint(1, 13)

    def get_points(self, higherOrLower):
        if ((higherOrLower == "l" and self.first_card > self.second_card) or
            (higherOrLower == "h" and self.first_card < self.second_card)):
            self.points = 100
        else:
            self.points = -75