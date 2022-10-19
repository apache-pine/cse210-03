import random


class Secret_word:

    def __init__(self):
        self._words = ['Award', 'Skill', 'Build', 'Teach', 'Doubt', 'Joint', 'Write',
                       'Phase', 'Front', 'Offer', 'Giant', 'Mouse', 'Scene', 'Night', 'Magic']
        self._secret_word = random.choice(self._words)

        self._secret_word = self._secret_word

    def select_word(self):
        secret_word = self._secret_word
        return secret_word

    def compare_guess(self, letter):
        if letter in self._secret_word:
            return True
        return False
