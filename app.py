from flask import Flask, request, jsonify
from funcs import commit_guess
import uuid

app = Flask(__name__)

TABLE = {}

ANS = 'attic'

start_msg = (
    "game {game_id} initiated. only 5 letter words supported (for now). "
    "the game lives at /game/{game_id}. "
    "GET requests report the status of the game. "
    "POST requests take your guess as data. "
)


@app.route('/', methods=['GET'])
def hello():
    if request.method == 'GET':
        data = "welcome to the wordle api. to get started hit the /start endpoint with a GET request"
        return jsonify(data)


@app.route('/start', methods=['GET'])
def start():
    if request.method == 'GET':
        game_id = str(uuid.uuid4())[:4]
        TABLE[game_id] = []
        data = start_msg.format(game_id=game_id)
        return jsonify(data)


@app.route('/game/<game_id>', methods=['GET', 'POST'])
def game(game_id):
    if request.method == 'GET':
        return jsonify(TABLE[game_id])
    elif request.method == 'POST':
        if len(TABLE[game_id]) == 5:
            return jsonify('game over! no more guesses allowed. you can start a new game at /start')
        guess = request.form.get('guess')
        if not guess:
            return jsonify('guess not received. remember to send guess=<your guess> as a key value pair')
        if len(guess) != 5:
            return jsonify('Guess should be 5 letters. Try again!')
        if '_' in guess:
            return jsonify('no underscores in guess')
        else:
            commit_guess(guess.lower(), ANS, game_id, TABLE)

        if TABLE[game_id][-1] == ['Y', 'Y', 'Y', 'Y', 'Y']:
            return jsonify(f'winner! {guess} was correct. issue a GET request to see your final score')
        else:
            return jsonify(TABLE[game_id])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
