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
        self.score = 0
        self.total_score = 300

        for i in range(1):
            card1 = Cards()
            self.card1.append(card1)

        for i in range(1):
            card2 = Cards()
            self.card2.append(card2)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.draw_cards()
            self.do_outputs()
            self.get_play()

    def get_play(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")

    def draw_cards(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
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
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your total score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
        