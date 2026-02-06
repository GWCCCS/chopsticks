import random, fingers

print()
print("o------------------------o")
print("| Welcome to Chopsticks! |")
print("o------------------------o")
print()

player1_name = input("Player 1, please enter your name:\n> ")
print("Hi", player1_name, "welcome to the game!")
print()

player2_name = input("Player 2, please enter your name:\n> ")
print("Hello", player2_name, "welcome to the game! (I like you better)")
print()

print("Who goes first?")
print("---------------")
print()

player1_diff = 0
player2_diff = 0

while player1_diff == player2_diff:
    target_number = random.randint(1, 100)

    print(player1_name, "pick your magic number from 1-100 (inclusive):")
    player1_guess = int(input("> "))
    print()

    print(player2_name, "pick your magic number from 1-100 (inclusive):")
    player2_guess = int(input("> "))
    print()

    player1_diff = abs(target_number - player1_guess)
    player2_diff = abs(target_number - player2_guess)

    if player1_diff == player2_diff:
        print("you guessed numbers within the same range of the target number aaaaaa!!!!!\n(guess again)\n")

player_index = 2
if player1_diff < player2_diff:
    player_index = 1

print("Player", player_index, "goes first!")
print()
