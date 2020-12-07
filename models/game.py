from models.game_classes import Player

rps = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def run_game(player1, player2):
    for key in rps:
        if key == player1.choice and rps[key] == player2.choice:
            # player1.wins += 1
            # player1.games +=1
            # player2.games += 1
            return f'{player1.name} wins'
        elif key == player2.choice and rps[key] == player1.choice:
            # player2.wins += 1
            # player1.games += 1
            # player2.games += 1
            return f'{player2.name} wins'
    if player1.choice == player2.choice:
        # player1.games +=1
        # player2.games += 1
        return 'Tie'
