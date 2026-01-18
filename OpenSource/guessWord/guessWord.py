import pandas as pd

class GuessWord:
    def __init__(self, word):
        self.word = word

    def initializer(self):
        print("Welcome to Guess the Word Game...")
        print("""
========================================
    Rules:
    - Select number of players
    - One of those playes will be selected randomly, and named as Knower
    - The knower will be the one to write the word to guess
    
    - The word selected will randomly shuffle.
    - The players each will have try to find the unknow word.
    - The knower does not participate in that round.
    
    - Each player have 10 points
    - The players will have the oportunity to normalize the word a little bit in order to have a hint. (-0.5 points per N)
    - The players will have the opportunity to quit if they dont know. (-1 Points)
    - After 10 trials, if the user does not match (-1 Points)
              
    - The program will dictate how many similarities do you have with the original word
              
    - Each player will have the opportunity to become The Knower
              
    - At the end will show statistics
    
""")
        self.players()

# Define the number of players
# 2 Players - 5 Players
    def players(self, number_players=None, sequence=None, players=None, players_pd=None):
        if sequence is None and players is None and players_pd is None:
            sequence = []
            players = []
            players_pd = []
        while True:
            if number_players is None:
                try:
                    number_players = int(input("Enter number of players: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
            if number_players <= 1 or number_players > 5:
                print("Invalid input. Enter a number between 2 and 5")
                number_players = None
            else:
                players = {f'Player_{i+1}': i for i in range(number_players)}
                # Check error
                players_pd = pd.DataFrame(players)
                print(players_pd)
                break
        

if __name__ == "__main__":
    MyApp = GuessWord("example")
    MyApp.initializer()