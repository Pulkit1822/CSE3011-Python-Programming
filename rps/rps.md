## Summary
The `determine_winner` function determines the winner of a rock-paper-scissors game between two players.

## Example Usage
```python
result = determine_winner("rock", "scissors")
print(result)
```
Output:
```
Player 1 wins.
```

## Code Analysis
### Inputs
- `player1` (string): The choice of player 1 (either "rock", "paper", or "scissors").
- `player2` (string): The choice of player 2 (either "rock", "paper", or "scissors").
___
### Flow
1. If `player1` and `player2` have the same choice, return "It's a tie."
2. If `player1` has "rock" and `player2` has "scissors", or if `player1` has "scissors" and `player2` has "paper", or if `player1` has "paper" and `player2` has "rock", return "Player 1 wins."
3. Otherwise, return "Player 2 wins."
___
### Outputs
- The function returns a string indicating the winner of the rock-paper-scissors game.
___
