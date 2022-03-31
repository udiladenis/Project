import random


def joc(x: list):
    y = str(input("Choose from list {}: ".format(x)))
    w = y
    z = random.choice(x)
    rez = None
    if y not in x:
        print("Invalid input!")

    if w == z:
        result = "Remiza"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    elif w == "Piatra" and z == "Foarfeca":
        result = "Piatra castiga!"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    elif w == "Piatra" and z == "Hartie":
        result = "Hartia castiga!"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    elif w == "Hartie" and z == "Foarfeca":
        result = "Foarfeca castiga!"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    elif w == "Hartie" and z == "Piatra":
        result = "Hartia castiga!"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    elif w == "Foarfeca" and z == "Piatra":
        result = "Piatra castiga!"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    elif w == "Foarfeca" and z == "Hartie":
        result = "Foarfeca castiga!"
        rez = ("\nJucatorul 1 a ales {}, \nJucatorul 2 a ales {}. \n\nRezultat: {}".format(w, z, result))
    return rez


lst = ["Piatra", "Hartie", "Foarfeca"]
print(joc(lst))
