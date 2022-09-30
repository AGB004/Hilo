from game.cards import Cards

class Director:
    
    def __init__(self):
        
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        self.cards = Cards()
        self.cards.draw()

    def start_game(self):
        
        while self.is_playing:
            self.get_input()
            self.do_outputs()
            self.get_play()

    def get_play(self):
        
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")

    def get_input(self):
        
        if not self.is_playing:
            return 

        print(f"The card is: {self.cards.first_card}")          

        guess = input("Higher or Lower? [h/l] ")
        self.score = 0

        """if draw_card.lower() == "h":
            for i in range(len(self.card2)):
                card2 = self.card2[i]
                card2.draw2()
                value = f"{card2.value2}"
                card2.calculate_hi()
                self.score += card2.points"""
        print(f"Next card is: {self.cards.second_card}")
        self.score = self.cards.get_points(guess)
        print(f"Round points: {self.score}") 
        self.total_score += self.score

    def do_outputs(self):
        
        print(f"Your total score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
        