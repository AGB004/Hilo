from game.cards import Cards

class Director:
    
    def __init__(self):
        
        self.card1 = []
        self.card2 = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        for i in range(1):
            card1 = Cards()
            self.card1.append(card1)

        for i in range(1):
            card2 = Cards()
            self.card2.append(card2)

    def start_game(self):
        
        while self.is_playing:
            self.draw_cards()
            self.do_outputs()
            self.get_play()

    def get_play(self):
        
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")

    def draw_cards(self):
        
        if not self.is_playing:
            return 

        for i in range(len(self.card1)):
            card1 = self.card1[i]
            card1.draw1()
            value = f"{card1.value1}"
        print(f"The card is: {value}")          

        draw_card = input("Higher or Lower? [h/l] ")
        self.score = 0

        if draw_card.lower() == "h":
            for i in range(len(self.card2)):
                card2 = self.card2[i]
                card2.draw2()
                value = f"{card2.value2}"
                card2.calculate_hi()
                self.score += card2.points
            print(f"Next card is: {value}")
            print(f"Round points: {self.score}") 
            self.total_score += self.score

        elif draw_card.lower() == "l":
            for i in range(len(self.card2)):
                card2 = self.card2[i]
                card2.draw2()
                value = f"{card2.value2}"
                card2.calculate_lo()
                self.score += card2.points
            print(f"Next card is: {value}")
            print(f"Round points: {self.score}") 
            self.total_score += self.score

    def do_outputs(self):
        
        print(f"Your total score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
        