from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
print(random_number)

@app.route('/')
def home():
    return '<h1> Guess a Number from 0-10 </h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def guessing(guess):
    if guess < random_number:
        return '<h1 style="color: red"> Too Low, guess again !! </h1>'\
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    
    elif guess > random_number:
        return '<h1 style="color: red"> Too High, guess again !!</h1>'\
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    
    else:
        return '<h1 style="color: green"> Correct Guess, Congratulations !!</h1>'\
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif ">'




if __name__ == '__main__':

    app.run(debug=True)
