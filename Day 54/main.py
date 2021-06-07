from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
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