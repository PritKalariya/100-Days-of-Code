from flask import Flask, render_template, request
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/form entry", methods=["GET", "POST"])
def receive_data():
    data = request.form
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=data["email"],
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Review\n\nName: {data['firstName']} {data['lastName']}\nEmail: {data['email']}\nMessage: {data['massage']}."
            )
        return f"<h1>Message Sent Successfully</h1>"
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)