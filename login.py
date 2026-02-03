import bcrypt 
import os 

USER_FILE = 'users.txt'


def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False
    
    with open(USER_FILE, 'r') as f:
        for line in f:
            if line.startswith(username + ':'):
                return True
    return False

def get_user_hash(username):
    f = open(USER_FILE, 'r')
    for line in f:
        saved_user, saved_hash = line.strip().split(':')
        if saved_user == username:
            return saved_hash.encode()
    return None
    f.close()

def register_user():
    print("\n=== User Registration ===")
    username = input("Enter username: ").strip()

    if user_exists(username):
        print("Username already exists")
        return 
    
    password = input("Enter password: ").encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    with open(USER_FILE, 'a') as f:
        f.write(f"{username}:{hashed.decode()}\n")
    print("Registration successful")

def login_user():
    print("\n=== User Login ===")
    username = input("Enter username: ").strip()

    if not user_exists(username):
        print("Username does not exist")
        return
    
    password = input("Enter password: ").encode()
    saved_hash = get_user_hash(username)

    if bcrypt.checkpw(password, saved_hash):
        print("Login successful")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
    