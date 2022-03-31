with open("Adrese.txt", "r") as files:
    files = files.read().splitlines()

# Function that write data into username text file
def write_data():
    bool = None
    with open("Adrese.txt", "a") as fil:
        adres = input("Enter account: ")
        if adres not in files:
            fil.write(f"{adres}\n")
            bool = True
        else:
            print("Data is already assigned")
            bool = False
    return bool



with open("Parole.txt", "r") as file:
    file = file.read().splitlines()

# Function that write data into password file
def write_pass():
    if write_data() == True:
        with open("Parole.txt", "a") as pas:
            i = input("Enter password: ")
            pas.write(f"{i}\n")


# With this function, we zip our username and password files to become like "username:password" -> dict tipe, so we can group them
def get_dict():
    rez = zip(files, file)
    return dict(rez)

# Function that return all our accounts WITHOUT PASSWORD, JUST ACCOUNT NAME
def shows_accounts():
    with open("Adrese.txt", "r") as files:
        files = files.read().splitlines()
        for i in files:
            print(i)