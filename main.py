import random

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

target_number = random.randint(1, 100)

print(player1_name, "pick your magic number from 1-100 (inclusive):")
player1_guess = int(input("> "))

diff = target_number - player1_guess

