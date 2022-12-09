"""
CS50x
"""
from cs50 import get_string

def meaw(n):
    """ printing cat sound """
    for i in range(n):
        print("meaw")

def calculator():
    """ calc docstring """
    try:
        x = int(input("x: "))
    except ValueError:
        print("That is not an int!")
        exit()
    try:
        y = int(input("y: "))
    except ValueError:
        print("That is not an int!")
        exit()
    print ("\nsum: ", x + y)
    print ("float division: ", x / y)
    print ("int division: ", x // y)

    z = x / y
    # This is a comment
    print (f"50 decimals error: {z: .50f}")

def agree():
    """ agree docstring  """
    s = get_string("Do you agree?").lower()

    if s in ["y", "yes"]:
        print("Agreed")
    elif s in ["n", "no"]:
        print("Not agreed")

def mario():
    """ Mario obstacle """
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    """ get height from user """
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
            print ("That is not an integer!")
    return n

def mario2():
    """ arguments example """
    for i in range(4):
        print ("?", end = "")
    print()
    print ("?" * 4)

def main():
    """ Main """
    mario2()

if __name__ == "__main__":
    main()
