
num_marks = 5
marks = []
grades = []

for i in range(num_marks):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

for mark in marks:
    if mark > 100:
        grades.append('Invalid Mark')
    elif mark > 75:
        grades.append('A')
    elif mark >= 65:
        grades.append('B')
    elif mark >= 55:
        grades.append('C')
    elif mark >= 45:
        grades.append('S')
    else:
        grades.append('F')
print("\nGrades:")
for i in range(5):
    print(f"Mark {marks[i]} ->  {grades[i]}")
