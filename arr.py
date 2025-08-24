import numpy as np
marks = np.array([45, 78, 62, 89, 90, 55, 38, 100, 67, 73,
                  82, 49, 95, 60, 71, 85, 77, 53, 92, 60])

print("Total no of students:", len(marks))

# print all marks with indexes
for i in range(0, len(marks)):
    print(f"Mark:{marks[i]}, Index:{i}")

# 5th student mark
print(marks[4])

# slice 5 to 10
print(marks[5:11])

# insert new mark 88 at 10th pos
print(np.insert(marks, 10, 88))

# append new mark 40 at end
print(np.append(marks, 40))

# delete first occurrence of 55
print(np.delete(marks, np.where(marks == 55)[0][0]))

# remove mark at index 3
print(np.delete(marks, 3))

# check if 100 exist
if 100 in marks:
    print("100 is present")
else:
    print("100 is not present")

# count how many scored exactly 90
print("No of students scored exactly 90:",np.count_nonzero(marks == 90))

# find index of first student who scored 71
for i in range(0, len(marks)):
    if marks[i] == 71:
        print("Index of the first student who scored 71:", i)
        break

# ascending order
print("Sorted marks in ascending order:", np.sort(marks))

# descending order
print("Sorted marks in descending order:", np.sort(marks)[::-1])

# reverse array
print("Reversed array:", marks[::-1])

# max and min
print(f"Maximum Mark:{marks.max()}, Minimum Mark:{marks.min()}")

# sum and average
print(f"Sum:{marks.sum()}, Avg:{marks.mean():.2f}")

# second highest and second lowest
sorted_marks = np.sort(marks)
print("Second highest:", sorted_marks[-2], "Second lowest:", sorted_marks[1])

# bottom 5 scores
print("Bottom 5 scores:", sorted_marks[:5])

# count how many >70
print("No of students scored more than 70:", np.count_nonzero(marks > 70))

# reshape into 4x5
reshaped = np.reshape(marks, (4, 5))
print("Reshaped into 4x5:\n", reshaped)

# split into 2 halves
a1, a2 = np.array_split(marks, 2)
print("First half:", a1)
print("Second half:", a2)

