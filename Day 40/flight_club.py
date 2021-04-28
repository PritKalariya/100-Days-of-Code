# This file is responsible for creating user profiles and sending them emails.
# Host this file and share this link with your friends.

import requests
import os
from dotenv import load_dotenv

load_dotenv()


print("Welcome to Prit's Flight Club ✈")
print("👨‍✈️: This is your captain speaking....I will help you find the best flight deals available.")
print("\nFill the below details to be a member!")

first_name = input("\nWhat is your first name?\n").title()
last_name = input("\nWhat is your last name?\n").title()

correct_email = False
while not correct_email:
    email1 = input("\nPlease enter your email addres.\n")
    email2 = input("\nPlease re-type your email address to confirm.\n")
    if email1 != email2:
      print("\n⚠ Email addresses do not match. Please re-enter")
    else:
      correct_email = True


new_member = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email1
    }
}


response = requests.post(
    url=os.getenv('SHEETY_USERS_ENDPOINT'),
    json=new_member
)


if response.status_code == 200:
    print("\nCongrats! You'r in the club.\n")
else:
    print(response.text)