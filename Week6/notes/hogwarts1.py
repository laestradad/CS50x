# Counts number of students in houses, using a DictReader

import csv

# Numbers of students in houses
houses = {
    "DIM": 0,
    "NAL": 0,
    "TOL": 0
}

# Count votes
with open("hogwarts.csv", "r") as file:
    reader = csv.DictReader(file)
    for item in reader:
        print(item)
    for row in reader:
        house = row["House"]
        houses[house] += 1

# Print counts
for house in houses:
    print(f"{house}: {houses[house]}")
