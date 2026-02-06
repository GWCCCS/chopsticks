"""The maximum amount of fingers that may be held up on one hand."""
MAX_FINGERS = 4

"""The template hands to be used for formatting utilities."""
HANDS_STR = """         ▄▄▄▄▄L4
 ░▒▓██████████▄L3
░▒▓██████ L ███L2
     ▀▀████████L1
        ▀▀▀▀▀╵
        ▄▄▄▄▄╷
     ▄▄████████R1
░▒▓██████ R ███R2
 ░▒▓██████████▀R3
         ▀▀▀▀▀R4"""

"""The str replacements to be used as fingers in the ``HANDS_STR`` template."""
LH_FINGER = "▄▄▄▄╷"
RH_FINGER = "▀▀▀▀╵"

def format_player(lh_amt: int, rh_amt: int) -> str:
    """Format the L/R hands of a single player, with hands facing rightward.

    :param lh_amt: The amount of fingers to lift on the LH.
    :param rh_amt: The amount of fingers to lift on the RH.
    :return:       The formatted string of the player's L/R hands.
    """
    hands_str = HANDS_STR # start with hands template str

    # lift LH's fingers
    for i in range(1, MAX_FINGERS+1):
        replacement = LH_FINGER if lh_amt >= i else "" # choose to use a finger or a blank str
        hands_str = hands_str.replace(f"L{i}", replacement) # make the replacement

    # lift RH's fingers
    for i in range(1, MAX_FINGERS+1):
        replacement = RH_FINGER if rh_amt >= i else "" # choose to use a finger or a blank str
        hands_str = hands_str.replace(f"R{i}", replacement) # make the replacement

    return hands_str

def format_players(
        player1_amts: tuple[int, int],
        player2_amts: tuple[int, int],
        padding: int = 4
) -> str:
    """Get the formatted hands of players 1 and 2 (left and right, respectively).

    :param player1_amts: The amount of player 1's fingers to hold up, as a tuple: (<LH#>, <RH#>)
    :param player2_amts: The amount of player 2's fingers to hold up, as a tuple: (<LH#>, <RH#>)
    :param padding:      (The amount of spaces between each the players' hands.)
    :return:             The formatted string of player 1 and 2's hands.
    """

    # get formatted player 1/2's hands, individually
    player1_str = format_player(*player1_amts)
    player2_str = format_player(*player2_amts[::-1])
    player2_str = player2_str.replace("L", "TEMP").replace("R", "L").replace("TEMP", "R")

    # split lines into lists
    left_side_split  = player1_str.split("\n")
    right_side_split = player2_str.split("\n")

    # find max line lengths
    max_left_len  = max([len(line) for line in left_side_split])
    max_right_len = max([len(line) for line in right_side_split])

    # combine player 1/2's hands
    full_split = [
        # format player 1 (left side)
        line.ljust(
            max_left_len + padding, " " # justify space to right of hands
        )
        # format player 2 (right side)
        + right_side_split[i][::-1].rjust( # get right side's line & reverse it
            max_right_len, " "             # justify space to left of hands
        )
        # loop through all left side lines
        for i, line in enumerate(left_side_split)
    ]

    return "\n".join(full_split) # return full_split joined by line breaks