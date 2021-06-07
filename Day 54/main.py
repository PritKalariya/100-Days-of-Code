from flask import Flask


app = Flask(__name__)


# Python decorators to stylr HTML elements
def make_bold(func):
    def wrapper_function():
        return "<b>" + func() + "</b>"
    return wrapper_function


# Decorator
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>This is testing paragraph.</p><br>' \
        '<img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width=300>'


# Applying the python decorators
@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"


# Add a variable section in the URL
# For more refer documentation https://flask.palletsprojects.com/en/1.1.x/quickstart/
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Grettings {name}!! You aare {number} years old."


if __name__ == "__main__":
    # Debug=TRUE will
    # 1. Activate the debugger
    # 2. Activate the automatic reloader
    # 3. Activates the debug mode on the flask application
    app.run(debug=True)