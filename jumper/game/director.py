from game.player import Player
from game.secret_word import Secret_word
from game.terminal_service import Terminal_service


class Director:

    def __init__(self):
        """Initializes the Director's objects."""
        self._player = Player()
        self._secret_word = Secret_word()
        self._terminal_service = Terminal_service()

        """Initializes the Director's variables."""
        self._keep_playing = self._player._keep_playing
        self._win = False
        pass

    def start_game(self):
        """Starts the game by running the main game loop."""
        while self._keep_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()

        """Checks to see if the player won or lost."""
        if self._win == False:
            print("Game over! You lost!")
        else:
            print("Game over! Congrats, You won!\n")

        """Asks user if they want to play again by calling the Player.play_again function."""
        self._keep_playing == Player.play_again()

        if self._keep_playing:
            self.start_game()
        else:
            pass
        pass

    def _get_inputs(self):
        """Calls the player objects method get_guess to get inputs."""
        self._guess = self._player.get_guess()
        pass

    def _do_updates(self):
        self._word = self._secret_word._secret_word

        if self._secret_word.compare_guess(self._guess):
            pass
        else:
            self._terminal_service.parachute.pop(0)

    def _do_outputs(self):
        self._terminal_service.word_display()
        self._terminal_service.display_parachute()
