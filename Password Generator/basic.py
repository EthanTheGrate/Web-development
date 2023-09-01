# isuppercase = bool(input("With uppercase letters?"))
# isnumbers = bool(input("With numbers?"))
# issymbols = bool(input("With symbols?"))
# length = int(input("How many characters do you want?"))

# print(isuppercase)
# print(isnumbers)
# print(issymbols)
# import random
# def generate_password():
#     choices = list("abcdefghijkmlopqrstuvxyz")

#     if isuppercase == True:
#         choices.extend("ABCDEFGHIJKLMOPQRSTUVWXYZ")
#     if isnumbers == True:
#         choices.extend("0123456789")
#     if issymbols == True:
#         choices.extend('''"'[]|\~!@#{}$/%^&*()_-+=<>,.:;?''')

#     mypassword = ""
#     for i in range(length):
#         mypassword += random.choice(choices)

#     print(mypassword)
# generate_password()

import random 
from flask import render_template, Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/fill_form')
def fill_form():
    return render_template('fill_form.html')


if __name__ == '__main__':
    app.run()