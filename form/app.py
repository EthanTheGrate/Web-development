from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

messages=[]
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    messages.append({"name": name, "email": email, "message": message})

    return redirect(url_for("thank_you"))

@app.route('/thank_you')
def thank_you():
    return "Celina is a mistake"

if __name__ == '__main__':
    app.run()