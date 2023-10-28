from flask import Flask, request, render_template

app = Flask(__name__)

quiz_question = "what is the capital of france?"
quiz_options = ["London", "Berlin", "Paris", "Delhi"]
correct_answer = "Paris"

@app.route('/')
def index():
    return "hi welcome to quiz application"

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        user_answer = request.form.get('answer')
        if user_answer == correct_answer:
            return "correct! paris is the capital of france"
        else:
            return "incorrect! try again!"
    return render_template('quiz.html', question=quiz_question, options=quiz_options)

if __name__ == '__main__':
    app.run(debug=True)