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

def main():
    register_user()

if __name__ == "__main__":
    main()