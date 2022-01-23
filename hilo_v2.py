# player starts with 300 points
# pick a random number between 1 and 13, and print that number
# player guesses if the next number is higher or lower
# if player guesses right, they gain 100 points
# if player guesses wrong, they lose 75 points
# if player points is 0 or less, they lose
# if player has more than 0 points, they can chose to keep playing
import random

# create two classes. One for card and one for game

# class for current card number and next card number


class Card():
    def __init__(self):
        # create random number between 1 and 13
        self.number = random.randint(1, 13)
        # create random number between 1 and 13, again
        self.next_number = random.randint(1, 13)
        # as long as the next number is not the same, don't continue
        while self.next_number == self.number:
            self.next_number = random.randint(1, 13)
        # print the card number
        print(f"The card is: {self.number}")

# class to handle the game


class Game():
    # create game
    def __init__(self, points):
        # call card class to get card numbers
        self.card = Card()
        self.player_points = points
        # ask for user guess
        self.player_guess = str(input("Higher or lower? [h/l]: "))

    # handling the guessing/points
    def check(self, player_guess):
        if player_guess == "h" and self.card.number > self.card.next_number:
            self.player_points += 100
            print(
                f"You guessed right! You now have {self.player_points} points.")
        elif player_guess == "l" and self.card.number < self.card.next_number:
            self.player_points += 100
            print(
                f"You guessed right! You now have {self.player_points} points.")
        else:
            self.player_points -= 75
            print(
                f"You guessed wrong! You now have {self.player_points} points.")
    # continue game or end game when needed/wanted

    def continue_game(self):
        if self.player_points <= 0:
            print(f"You lost! You now have {self.player_points} points.")
            return False
        elif str(input("Do you want to keep playing? [y/n]: ")) == "n":
            return False


# main function to start the game
def main(points):
    game = Game(points)
    game.check(game.player_guess)
    while True:
        con = game.continue_game()
        if con == False:
            break
        else:
            game = Game(game.player_points)
            game.check(game.player_guess)

    print("Thanks for playing!")


# calling main function and starting the game with 3oo points
main(300)
