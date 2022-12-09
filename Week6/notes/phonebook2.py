import csv
from cs50 import get_string

name = get_string("Name: ")
number = get_string("Number: ")

with open("phonebook.csv", newline='', encoding="utf-8", mode="a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])
