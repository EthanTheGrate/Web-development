from flask import Flask, render_template

app = Flask(__name__)

leaderboard = [
    {'username': 'User1', 'score': 100},
    {'username': 'User2', 'score': 95},
    {'username': 'User3', 'score': 90},
    {'username': 'User4', 'score': 85},
    {'username': 'User5', 'score': 80},
]

@app.route('/')
def index():
    return "leaderboard app gawk gawk"

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)