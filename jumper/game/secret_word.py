import random


class Secret_word:

    def __init__(self):
        self.words = ['Award', 'Skill', 'Build', 'Teach', 'Doubt', 'Joint', 'Write',
                      'Phase', 'Front', 'Offer', 'Giant', 'Mouse', 'Scene', 'Night', 'Magic']
        self.secret_word = random.choice(self.words)

        self.secret_word = self.secret_word

    def select_word(self):
        secret_word = self.secret_word
        return secret_word

    def compare_guess(self, letter):
        if letter in self.secret_word:
            return True
        return False
