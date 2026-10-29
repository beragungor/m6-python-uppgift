import json
import bcrypt

with open("users.json", "r") as file:
    users = json.load(file)

def login():
    while True:
        username = input("What's your username? ") 
        password = input("What's your password? ")  
        if username in users and bcrypt.checkpw(password.encode("utf-8"),
            users[username]["password"].encode("utf-8")):
            print("\nLogin successfull!\n")
            return True

        else: 
            print("\nWrong username or password. What do you want to do?")
            
            while True:
                reg = input("    Register a new one (r)\n    Try again (t)\n    Use Bikeability (b)\nOption: ").strip().lower()

                if reg == "r":
                    register()
                    break

                elif reg == "t":
                    break

                elif reg == "b":
                    return False

                else:
                    print("Please choose a valid option!")

def register():
    username = input("Choose your username: ")
    if username in users:
        print("Username already exists!")

    password = input("Choose your password: ")

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    users[username] = {"password" : password_hash}
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
    print("Registration successful!")
    return
    
if __name__ == "__main__":
    login()