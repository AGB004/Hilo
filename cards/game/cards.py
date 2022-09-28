import random

class Cards():
    
    def __init__(self):
       
        self.value1 = 0
        self.value2 = 0
        self.points = 0

    def draw1(self):
        
        self.value1 = random.randint(1, 13)
    
    def draw2(self):
        
        self.value2 = random.randint(1, 13)

    def calculate_hi(self):
          
        if self.value1 < self.value2:
            self.points = 100
        elif self.value1 > self.value2:
            self.points = -75
        else:
            self.points = 0

    def calculate_lo(self):
         
        if self.value1 > self.value2:
            self.points = 100
        elif self.value1 < self.value2:
            self.points = -75
        else:
            self.points = 0

