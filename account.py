import json

with open("users.json", "r") as file:
    users = json.load(file)

def login():
    username = input("What's your username? ")
    if username not in users:
        reg = input("\nNo account found with that username, do you want to register a new one?\n    Register (y)\n    Try again (n)\n    Quit (q)\nOption: ")
    password = input("What's your password?")

    if username in users:
        print("Account found")
        


login()
