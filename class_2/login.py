username = "admin"
password = "1234"

user_input = input()
password_input = input()

if user_input == username and password_input == password:
    print(f"Login successful")
else:
    print(f"Login failed")