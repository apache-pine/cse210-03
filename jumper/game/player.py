class Player:
    def __init__(self):
        self.guess = ""
        self.keep_playing = True
        pass

    '''
    Get a letter guess from the user. If the user enters a number or multiple letters
    they will be asked again.
    '''
    def get_guess(self):
        valid = False
        while(valid != True):
            self.guess = input("Guess a letter [a-z]: ")

            '''Validate user response'''
            if (len(self.guess) != 1):
                print("Invalid input please try again with a single letter")
                valid = False
            elif (self.guess.isnumeric()):
                print("Invalid input numbers are not allowed")
                valid = False
            else:
                valid = True

        return self.guess

        
    '''
    Ask the user if they want to play again.
    '''
    def play_again(self):
        valid = False
        while(valid == False):
            '''Get input'''
            response = input("Would you like to play again [y/n]? ")

            '''Validate user response'''
            if (len(response) != 1):
                valid = False
            elif (response.isnumeric()):
                print("Invalid response")
                valid = False
            elif (response.lower() == "y" or response.lower() == "n"):
                valid = True
            else:
                print("Invalid response")
                valid = False
            
        '''If user response is valid get keep_playing value'''
        if response.lower() == "y":
            self.keep_playing = True
        else:
            self.keep_playing = False

        return self.keep_playing