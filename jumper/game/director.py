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
        self._letter_list = []
        self._word_list = self._terminal_service.word_list
        self._num_bad_guesses = 0
        self._secret_word_list = []
        pass

    def start_game(self):
        """Starts the game by running the main game loop."""
        self._word = self._secret_word._secret_word
        self._word_check = self._secret_word._secret_word
        while self._keep_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()

        """Checks to see if the player won or lost."""
        if self._win == False:
            print("\nGame over! You lost!")
        else:
            print("\nGame over! Congrats, You won!\n")

        """Asks user if they want to play again by calling the Player.play_again function."""
        self._keep_playing == Player.play_again()

        if self._keep_playing:
            self.start_game()
        else:
            pass
        pass

    def _get_inputs(self):
        """Calls the player objects method get_guess to get inputs."""
        if self._word != "":
            self._guess = self._player.get_guess()
        else:
            pass

    def _do_updates(self):
        self._letter_list.append(self._guess)

        if self._word != "":
            if self._secret_word.compare_guess(self._guess):
                while self._guess in self._word:
                    index = self._word_check.index(self._guess)
                    self._word_list[index] = self._guess
                    self._word = self._word.replace(self._guess, "", 1)
                    self._word_check = self._word_check.replace(
                        self._guess, "_", 1)
            else:
                self._terminal_service.parachute.pop(1)
                self._num_bad_guesses += 1
                if self._num_bad_guesses == 4:
                    self._keep_playing = False
                    self._win = False
        else:
            self._keep_playing = False
            self._win = True

    def _do_outputs(self):
        self._terminal_service.word_display()
        self._terminal_service.display_parachute()
        if self._letter_list != []:
            print("Letters guessed: ")
            self._terminal_service.display_guesses(self._letter_list)
        else:
            pass
