names = ("Dan", "George", "Yosi", "Guy", "Noam")


user_name = input("Enter your name: ").strip().lower()


if user_name in [name.lower() for name in names]:
    print(f"Welcome, {user_name.capitalize()}! You are on the list.")
else:
    print("Sorry, you are not on the list.")
    
    