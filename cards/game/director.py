from game.cards import Cards


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card1 = []
        self.card2 = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0

        for i in range(1):
            card = Cards()
            self.card1.append(card)

        for i in range(1):
            card = Cards()
            self.card2.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.draw_card1()
            self.draw_card2()
            self.do_outputs()
            self.get_play()

    def get_play(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")

    def draw_card1(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.card1)):
            card = self.card1[i]
            card.draw()
            print(f"The card is: {card.value1}")          

    def draw_card2(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Higher or Lower? [h/l] ")
        
        if draw_card.lower == "h":
            for i in range(len(self.card2)):
                card = self.card2[i]
                card.draw()
                print(f"Next card is: {card.value2}")
                card.calculate_hi()
                self.score += card.points 
            self.total_score += self.score

        elif draw_card.lower == "l":
            for i in range(len(self.card2)):
                card = self.card2[i]
                card.draw()
                print(f"Next card is: {card.value2}")
                card.calculate_hi()
                self.score += card.points
            self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        self.total_score = 0
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
        