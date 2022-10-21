class Terminal_service:
    '''Class that performs all of the services regarding the '''

    def __init__(self):
        self.parachute = [' ', '  ___  ', ' /___\\ ', ' \\   / ', '  \\ /  ', '   0   ', '  /|\\  ', '  / \\  ', '', '^^^^^^^']
        self.word_list = ['_', '_', '_', '_', '_']

    def display_parachute(self):
        '''Create and print parachute as a list that can then be manipulated by the
        directer class to remove the first 4 list items as the player guesses wrong.'''
        for each in self.parachute:
            print(each)

    def word_display(self):
        '''Print the inital word display with blank spaces to be used by the user
        for guessing.'''
        word_as_string = ''
        for each in self.word_list:
            word_as_string += each + ' '

        return print(word_as_string)

    def display_guesses(self, letter_list):
        '''Print the necassary letter spaces and word. Accepts a list of
        letters as a parameter in order to print each new letter that is 
        guessed correctly.'''
        word_guessed = ''

        for each in letter_list:
            word_guessed += f'{each}, '
        print(word_guessed)
