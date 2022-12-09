import csv
from cs50 import get_string

file = open("phonebook.csv", newline='', encoding="utf-8", mode="a")
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exist

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()
