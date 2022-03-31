import Functions

class Password_manager:
    def start():
        print("Hello there. This is your personal password manager!")
        print("This manager is like your best friend that you can count on because if you forget something, he will be there for you :)")
        print("So let start!")
        print("This is suposed to be on your local computer so you should be the only user that have acces to your own passwords or protected data!")
        print("All you have to do is to insert your adress that u need password for and the manager will give it to you! Hope you will like it :) ", end = "\n")

    
    def insert_data():
        return Functions.write_pass()

    def get_passwords():
        print("\nFor whitch of these accounts do u need password?: ")
        Functions.shows_accounts()
        email = input("\nEnter account name: ")
        if email in Functions.get_dict():
            return Functions.get_dict()[email]
        else:
            return ("Invalid data!")

    def menu():
        print("\n1. Insert new data")
        print("2. Get passsword")
        print("3.Quit")

m = Password_manager

m.start()
m.menu()


while True:
    choice = int(input("Enter your option: "))
    if choice == 1:
        m.insert_data()
        break # break point so that new asigned data could be saved and we can get the password for that new account
    elif choice == 2:
        print(m.get_passwords())
    else:
        quit()
