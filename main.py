# dep

import random, fingers


# init


# main

def game():
    # init

    players = [
        {
            "name": "NA",
            "hands": [1, 1]
        },
        {
            "name": "NA",
            "hands": [1, 1]
        }
    ]

    rounds_count = 0
    windex = -1

    # "main menu" thing

    print("\no————————————————————————o")
    print("| Welcome to Chopsticks! |")
    print("o————————————————————————o\n")

    print("Enter your names!")
    print("—————————————————\n")

    players[0]["name"] = input("Player 1:\n> ")
    print(f"Hi {players[0]["name"]} welcome to the game!\n")

    players[1]["name"] = input("Player 2:\n> ")
    print(f"Hello {players[1]["name"]} welcome to the game! (I like you better)\n")

    print("Who goes first?")
    print("———————————————\n")

    player1_dist = 0
    player2_dist = 0

    while player1_dist == player2_dist:
        target_number = random.randint(1, 100)

        print(players[0]["name"], "pick your magic number from 1-100 (inclusive):")
        player1_guess = int(input("> "))
        print()

        print(players[1]["name"], "pick your magic number from 1-100 (inclusive):")
        player2_guess = int(input("> "))
        print()

        player1_dist = abs(target_number - player1_guess)
        player2_dist = abs(target_number - player2_guess)

        if player1_dist == player2_dist:
            print("you guessed numbers within the same range of the target number aaaaaa!!!!!\n(guess again)\n")

    player_idx = 0
    if player1_dist > player2_dist:
        player_idx = 1

    print(f"Player {players[player_idx]["name"]} goes first!\n")

    # game loop

    while True:
        rounds_count += 1
        round_title = f"-*- ROUND {rounds_count}!!! -*-"
        round_title_line = f"o{"".ljust(len(round_title) + 2, "—")}o"
        print(f"{round_title_line}\n| {round_title} |\n{round_title_line}\n")

        print(f"{players[0]["name"]} (P1) vs. {players[1]["name"]} (P2)")
        print(
            fingers.format_players(
                tuple(players[0]["hands"]),
                tuple(players[1]["hands"])
            )
        )

        # util vars

        player = players[player_idx]
        hands = player["hands"]

        other_player_idx = (player_idx + 1) % 2
        other_player = players[other_player_idx]
        other_hands  = other_player["hands"]

        # win condition

        if sum(hands) == 0: windex = other_player_idx
        elif sum(other_hands) == 0: windex = player_idx
        if windex != -1: break

        # choose action

        print(f"\n{player["name"]} please choose an action:")
        print("1: Merge")
        print("2: Transfer")

        action = "NA"
        while action not in [ "1", "2" ]:
            action = input("> ")
        print()

        # do actions

        # merge
        if action == "1":
            if hands in [ (1, 0), (0, 1) ]: # merging not allowed
                action = "2"
            else:
                merge = "LTR" if hands[1] == 0 else ("RTL" if hands[0] == 0 else "NA")

                if merge == "NA":
                    print("Merging left-to-right (LTR) or right-to-left (RTL)?")
                    while merge not in [ "LTR", "RTL" ]:
                        merge = input("> ").upper()
                else:
                    print(f"Merging direction: {merge} (auto-selected)")

                from_idx = 0 if merge == "LTR" else 1
                to_idx  = (from_idx + 1) % 2

                from_amt, to_amt = hands[from_idx], hands[to_idx]

                from_max = min(from_amt, 4 - to_amt)

                print("How many fingers to merge?")
                merge_amt = 0
                print(from_amt, to_amt)
                while not (0 < merge_amt <= from_max):
                    merge_amt = input("> ")
                    try:
                        merge_amt = int(merge_amt)
                    except ValueError:
                        merge_amt = 0

                if merge == "LTR":
                    player["hands"] = [
                        hands[0] - merge_amt,
                        hands[1] + merge_amt
                    ]
                else:
                    player["hands"] = [
                        hands[0] + merge_amt,
                        hands[1] - merge_amt
                    ]

        # transfer
        if action == "2":
            from_idx = 0 if hands[1] == 0 else (1 if hands[0] == 0 else -1)
            if from_idx == -1:
                print("Transferring from your left hand (L) or right hand (R)?")
                while from_idx == -1:
                    from_side = input("> ").upper()
                    from_idx = 0 if from_side == "L" else (1 if from_side == "R" else -1)
            else:
                print(f"Transferring from your {"left" if from_idx == 0 else "right"} hand (auto-selected)")
            print()

            to_idx = 0 if other_hands[1] == 0 else (1 if other_hands[0] == 0 else -1)
            if to_idx == -1:
                print(f"Transferring to {other_player["name"]}'s left hand (L) or right hand (R)?")
                while to_idx == -1:
                    to_side = input("> ").upper()
                    to_idx = 0 if to_side == "L" else (1 if to_side == "R" else -1)
            else:
                print(f"Transferring to {other_player["name"]}'s {"left" if from_idx == 0 else "right"} hand (auto-selected)")

            other_hands[to_idx] += hands[from_idx]
            if other_hands[to_idx] >= 5: other_hands[to_idx] = 0

        # next player
        player_idx = (player_idx + 1) % 2

    print("\nThe game has ended......")
    print("————————————————————————\n")

    print(f"{players[windex]["name"]} won in {rounds_count} rounds!!!!\nCongratulations!!!!!!!!!!!!\n\n")
    input("(press enter to end)\n")

# main

if __name__ == "__main__":
    game()