def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie."
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins."
    else:
        return "Player 2 wins."

if __name__ == "__main__":
    player1 = input("Player 1? ").lower()
    player2 = input("Player 2? ").lower()
    result = determine_winner(player1, player2)
    print(result)
