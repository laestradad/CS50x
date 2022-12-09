import sys

numbers = [1, 3, 5, 6, 3, 0]

if 0 in numbers:
    print("Found!")
    sys.exit(0)

print("Not found")
sys.exit(1)
