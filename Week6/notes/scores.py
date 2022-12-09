from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Enter score: ")
    scores += [score] #concatenate lists

average = sum(scores) / len(scores) #sum array elements
print(f"Average: {average}")