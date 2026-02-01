# CHOPSTICKS

### Premise:
- 2 players, each starting with one finger on each hand
- Make the opponent lost both hands
  - \>=5 fingers on each hand

### Types of Actions (1 action per turn):
- "Merge"
  - Combine # of fingers into one hand
- "Transfer"
  - Choose one of own hands to transfer FROM
  - Choose an opponent's hand to transfer TO

### Game Steps/Timeline:
- Title Screen
  - (e.g. "Welcome to Chopsticks!")
- Prompt for players' names
- Choose who goes first
  - Whoever guesses closest to a random number
  - Rock paper scissors
- LOOP:
    - Hands displayed (however that ends up working)
    - Current player prompt:
        - Pick an action, "Merge" or "Transfer"
    - For "Merge"
        - LTR or LTR
    - For "Transfer"
        - Pick own L/R hand
        - Pick opponent's L/R hand
    - Check if a player has lost/won (a hand is >=5 fingers)
        - If a player has lost/won:
            - Display win message
            - Play again prompt
    - Switch to next player