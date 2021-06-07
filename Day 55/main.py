# A number guessing using flask.
# Run the python script go to URL and add '/<number>' to guess the number


from flask import Flask
import random


random_number = random.randint(1, 9)


app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1><b>Guess a number between 1 and 9</b></h1><br>'\
    '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif">'


@app.route('/<int:number>')
def check_number(number):
    if number < random_number:
        return '<h1 style="color: yellow"><b>Guessed too low</b></h1><br>'\
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number:
        return '<h1 style="color: red"><b>Guessed too High</b></h1><br>'\
        '<img src="https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif">'
    else:
        return '<h1 style="color: green"><b>Correct Answer</b></h1><br>'\
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == '__main__':
    app.run(debug=True)