def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "fail"

students = []
while True:

    name = input("enter student name:")

    marks1 = float(input("enter marks for subject 1:"))
    marks2 = float(input("enter marks for subject 2:"))
    marks3 = float(input("enter marks for subject 3:"))
    marks4 = float(input("enter marks for subject 4:"))
    total = marks1 + marks2 + marks3 + marks4
    average = total / 4

    grade = calculate_grade(average)
    students.append([name, total, average, grade])
    choice = input("do you want to add another:enter 'yes' or 'no'")
    if choice.lower() != "yes":
        break
print("\n-----student report-----")
for student in students:
    print("name:", students[0])
    print("total:", students[1])
    print("average:", student[2])
    print("grade", student[3])
    print("--------------------------------")