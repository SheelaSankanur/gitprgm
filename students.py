students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 78)
]

# Sort by marks (second element)
sorted_by_marks = sorted(students, key=lambda x: x[1])
print(sorted_by_marks)
# [('Charlie', 78), ('Alice', 85), ('Bob', 90)]