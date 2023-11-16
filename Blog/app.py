from flask import Flask, render_template, url_for

app = Flask(__name__)

leaderboard_list = [
    {'username' : 'Baodan', 'grade' : 69, 'age' : 420},
    {'username' : 'Ethan', 'grade' : 8, 'age' : 13},
    {'username' : 'Celina', 'grade' : -3, 'age' : -8},
    {'username' : 'Angelina', 'grade' : 1, 'age' : 6}
]

@app.route('/students')
def leaderboard():
    return render_template('students.html', leaderboard=leaderboard_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)