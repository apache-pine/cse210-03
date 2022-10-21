class Terminal_service:
    '''Class that performs all of the services regarding the '''
    def __init__(self):

        self.parachute = ['  ___  ', ' /___\\ ', ' \\   / ', '  \\ /  ', '   0   ', '  /|\\  ', '  / \\  ', '', '^^^^^^^']
        self.word_display = ['_', '_', '_', '_', '_']

    def display_parachute(self):
        '''Create and print parachute as a list that can then be manipulated by the
        directer class to remove the first 4 list items as the player guesses wrong.'''
        word_as_string = ''
        for each in self.parachute:
            word_as_string += each + ' '
        
        return print(word_as_string)
            

    def word_display(self):
        '''Print the inital word display with blank spaces to be used by the user
        for guessing.'''
        for each in self.word_display:
            print(each)

    def get_input(self, prompt):
        '''Gets the user input and directs the user with the given prompt'''
        return input(prompt)

    # def display_word(self, word):
    #     '''Convert the word through an argument to be used in a list by the director class, as well as 
    #     the display word method. The word'''
    #     self.word = word

    #     for each in self.word:
    #         self.word_letters.append(each)
        
    #     return self.word_letters

    def display_guesses(self, letter_list):
        '''Print the necassary letter spaces and word. Accepts a list of
        letters as a parameter in order to print each new letter that is 
        guessed correctly.'''
        word_guessed = ''

        for each in letter_list:
            word_guessed += f'{each} '
        print(word_guessed)
