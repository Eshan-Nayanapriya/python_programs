
num_students = 10
marks = []

for i in range(num_students):
    mark = int(input(f"Enter mark for student {i+1}: "))
    marks.append(mark)
    
max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) / num_students

print(f"Maximum mark: {max_mark}")
print(f"Minimum mark: {min_mark}")
print(f"Average mark: {avg_mark:.2f}")
