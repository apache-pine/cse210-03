import random


class Secret_word:

    def __init__(self):
        self._words = ['award', 'skill', 'build', 'teach', 'doubt', 'joint', 'write',
                       'phase', 'front', 'offer', 'giant', 'mouse', 'scene', 'night', 'magic']
        self._secret_word = random.choice(self._words)

        self._secret_word = self._secret_word

    def select_word(self):
        secret_word = self._secret_word
        return secret_word

    def compare_guess(self, letter):
        if letter in self._secret_word:
            return True
        return False
