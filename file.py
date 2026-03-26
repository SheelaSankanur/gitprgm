#for loop next()
with open(r"C:\Users\ganes\OneDrive\Desktop\python\data.txt","r") as file:
    for i in file:
        print(i)

#while loop
with open(r"C:\Users\ganes\OneDrive\Desktop\python\data.txt","r") as file:
    while True:
        try:
            line=next(file)
            print(line)
        except StopIteration:
            print("file content over")
            break 

