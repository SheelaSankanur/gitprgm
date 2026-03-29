
marks=[92,86,87,85,56]
marks.append(48)
print(marks)
marks.remove(56)
print(marks)
marks=[]
for i in range(5):
    m=int(input("enter marks:"))
    marks.append(m)
print("all marks",marks)
print("highest",max(marks))
print("lowest",min(marks))