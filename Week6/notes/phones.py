""" docstring """
from sys import exit
from cs50 import get_string

people = {
    "Luis": "999999",
    "Dave": "111111"
}

name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")
    exit(0)
exit(1)
