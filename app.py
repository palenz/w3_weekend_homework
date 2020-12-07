from flask import Flask
from flask import render_template, request, redirect
from models.game import run_game
from models.game_classes import Player

app = Flask(__name__)

player1_wins = 0
player2_wins = 0

@app.route('/')
def index():
    return render_template('index.html', title='home')

@app.route('/play', methods=['POST'])
def play():

    player1_name = request.form['player1_name']
    player1_move = request.form['player1']
    player2_name = request.form['player2_name']
    player2_move = request.form['player2']

    player1 = Player(name=player1_name, choice=player1_move)
    player2 = Player(name=player2_name, choice=player2_move)

    result = run_game(player1, player2)

    return render_template('results.html', title='results', result=result, player1=player1, player2=player2)

if __name__ == '__main__':
    app.run(debug=True)