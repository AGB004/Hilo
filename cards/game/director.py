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
            self.get_play()
            self.draw_card1()
            self.make_guess()
            self.draw_card2()
            self.do_outputs()

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

        for i in range(len(self.cards)):
            card = self.card1[i]
            card.draw()

    def make_guess(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        print(f"The card is: {self.card1}")
        draw_card = input("Higher or Lower? [h/l] ")
        self.is_playing = (draw_card == "y")            

    def draw_card2(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.cards)):
            card = self.card1[i]
            card.draw()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing = (self.score > 0)
        