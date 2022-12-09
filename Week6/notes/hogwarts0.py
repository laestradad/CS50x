# Counts number of students in houses

import csv

# Numbers of students in houses
houses = {
    "DIM": 0,
    "NAL": 0,
    "TOL": 0
}

# Count votes
with open("hogwarts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #skip first row
    for row in reader:
        print(row)
        house = row[1]
        houses[house] += 1

# Print counts
for house in houses.keys():
    print(f"{house}: {houses[house]}")
